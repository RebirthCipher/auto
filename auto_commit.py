import os
import subprocess
import datetime

# --- CONFIG ---
REPO_PATH = "/home/lordwhitefire/projects1/inspect-test"
DUMMY_FILE = "auto_log.txt"
TOTAL_COMMITS = 10000
COMMITS_PER_PUSH = 500  # Push every 500 commits
# ---------------

os.chdir(REPO_PATH)

print("🚀 Starting auto commits...")

for i in range(1, TOTAL_COMMITS + 1):
    with open(DUMMY_FILE, "a") as f:
        f.write(f"Commit #{i} - {datetime.datetime.now()}\n")

    subprocess.run(["git", "add", DUMMY_FILE], check=True)
    subprocess.run(["git", "commit", "-m", f"Auto Commit #{i}"], check=True)

    if i % COMMITS_PER_PUSH == 0 or i == TOTAL_COMMITS:
        print(f"📤 Pushing at commit #{i}...")
        subprocess.run(["git", "push", "origin", "main"], check=True)

print("✅ Done! All commits made and pushed.")
