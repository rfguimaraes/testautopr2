import sys
import git

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <remote_name>")
    sys.exit(1)

# Get the remote name from the command-line argument
remote_name = sys.argv[1]

# Open the Git repository in the current directory
repo = git.Repo(".")

custom_author = git.Actor("Your Custom Author Name", "custom.author@example.com")
custom_committer = git.Actor("Your Custom Committer Name", "custom.committer@example.com")

# Stage all changes
repo.git.add("--all")

# Commit the changes
commit_message = "Your commit message here"
repo.index.commit(commit_message, author=custom_author, committer=custom_committer)

# Push the changes to the specified remote and branch
current_branch = repo.active_branch
remote = repo.remotes[remote_name]
remote.push(current_branch)

print(f"Changes staged, committed, and pushed to '{remote_name}/{current_branch}'")
