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


# Get the author's name and email from the Git configuration
config = repo.config_reader()
author_name = config.get_value("user", "name")
author_email = config.get_value("user", "email")


print(f"Author Name: {author_name}")
print(f"Author Email: {author_email}")

custom_author = git.Actor("Your Custom Author Name", "custom.author@example.com")

# Stage all changes
repo.git.add("--all")

# Commit the changes
commit_message = "Your commit message here"
repo.index.commit(commit_message)

# Push the changes to the specified remote and branch
current_branch = repo.active_branch
remote = repo.remotes[remote_name]
remote.push(current_branch)

print(f"Changes staged, committed, and pushed to '{remote_name}/{current_branch}'")
