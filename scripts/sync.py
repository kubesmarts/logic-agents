"""Copy the shared instructions and skill from this checkout's committed HEAD."""
import argparse
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("repo", type=Path)
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
source = Path(__file__).resolve().parents[1]
target = args.repo.resolve()
if not (target / ".git").exists() or source == target:
    parser.error("choose a separate product repository root")

def git(*args):
    return subprocess.check_output(["git", "-C", str(source), *args])

revision = git("rev-parse", "HEAD").decode().strip()
skill = ".agents/skills/prepare-pr"
paths = git("ls-tree", "-r", "--name-only", revision, skill).decode().splitlines()
files = {".logic-agents/AGENTS.md": git("show", f"{revision}:AGENTS.md")}
files.update({p: git("show", f"{revision}:{p}") for p in paths})
files[".logic-agents/revision"] = (revision + "\n").encode()
dirty = False
for path, content in files.items():
    output = target / path
    if output.is_file() and output.read_bytes() == content:
        continue
    print(path)
    dirty = True
    if not args.check:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
sys.exit(int(args.check and dirty))
