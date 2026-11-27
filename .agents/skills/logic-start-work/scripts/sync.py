"""Refresh ignored Logic guidance from a canonical logic-agents checkout."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("repo", type=Path)
parser.add_argument("--check", action="store_true")
parser.add_argument("--pre-pr", action="store_true", help="check this source against published main before syncing")
args = parser.parse_args()
source = Path(__file__).resolve().parents[4]
target = args.repo.resolve()
if not (source / "CONTRIBUTING.md").is_file() or not (target / ".git").exists():
    parser.error("run the script from logic-agents and pass a product repository root")
if args.pre_pr:
    upstream = "https://github.com/kubesmarts/logic-agents.git"
    git = ["git", "-C", str(source)]
    published = subprocess.check_output([*git, "ls-remote", "--exit-code", upstream, "refs/heads/main"]).split()[0].decode()
    head = subprocess.check_output([*git, "rev-parse", "HEAD"], text=True).strip()
    if head != published:
        contains_main = subprocess.run([*git, "merge-base", "--is-ancestor", published, head])
        if contains_main.returncode:
            sys.exit(f"Cannot confirm this checkout includes published main {published}. Update your source checkout before preparing the PR.")
        print(f"Using local development revision {head} ahead of published main {published}.")
    if subprocess.check_output([*git, "status", "--porcelain", "--", "AGENTS.md", ".agents/skills"]):
        print("Using uncommitted shared guidance from the source checkout.")

if source == target:
    sys.exit(0)

revision = subprocess.check_output(["git", "-C", source, "rev-parse", "HEAD"])
files = {Path(".logic-agents/AGENTS.md"): (source / "AGENTS.md").read_bytes(),
         Path(".logic-agents/revision"): revision}
for skill in sorted((source / ".agents/skills").glob("logic-*")):
    if not (skill / "SKILL.md").is_file():
        continue
    for path in skill.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts:
            files[path.relative_to(source)] = path.read_bytes()

# Only retire files recorded by an earlier sync. Preserve hand-written skills.
manifest = Path(".logic-agents/installed.json")
manifest_file = target / manifest
installed = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
current = {str(path): hashlib.sha256(content).hexdigest()
           for path, content in files.items() if path.parts[:2] == (".agents", "skills")}
files[manifest] = (json.dumps(current, indent=2, sort_keys=True) + "\n").encode()
retired = []
for key in installed.keys() - current.keys():
    path = Path(key)
    if path.parts[:2] != (".agents", "skills") or len(path.parts) < 4 or not path.parts[2].startswith("logic-") or ".." in path.parts:
        sys.exit(f"Invalid managed skill path: {key}")
    dest = target / path
    if dest.resolve() != dest:
        sys.exit(f"Refusing to remove a symlinked skill path: {path}")
    if dest.exists():
        if hashlib.sha256(dest.read_bytes()).hexdigest() != installed[key]:
            sys.exit(f"Retired skill file has local edits: {path}. Move it aside before syncing.")
        retired.append(dest)

different = bool(retired)
for dest in retired:
    print(f"Retired: {dest.relative_to(target)}")
    if not args.check:
        dest.unlink()

for relative, content in files.items():
    destination = target / relative
    if destination.resolve() != destination:
        sys.exit(f"Refusing to write through a symlink: {relative}")
    if destination.is_file() and destination.read_bytes() == content:
        continue
    print(relative)
    different = True
    if not args.check:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
sys.exit(int(args.check and different))
