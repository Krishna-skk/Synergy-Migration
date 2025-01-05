import subprocess

# Define commit messages (Synergy's "list-changes.txt")
changes = [
    "Initial commit for file1 and file2.",
    "Fixed bug in file1.c.",
    "Added new feature to file2.c."
]

# Define the files to be tracked (Synergy's "list-files.txt")
files = [
    ("file1.c", "// file1.c - Initial version"),
    ("file2.c", "// file2.c - Initial version")
]

# Create a new fast-import file to simulate the import
with open('synergy-to-git.import', 'w') as output:
    for i, change in enumerate(changes):
        # Write the commit message for each change
        commit_message = change
        output.write(f"commit refs/heads/master\n")
        output.write(f"mark :{i + 1}\n")
        output.write(f"author Synergy User <user@example.com> 1613000000 +0000\n")
        output.write(f"committer Synergy User <user@example.com> 1613000000 +0000\n")
        output.write(f"\n")
        output.write(f"data {len(commit_message)}\n")
        output.write(f"{commit_message}\n")
        output.write(f"###\n")

        # Simulate adding files and their contents (from Synergy)
        for file_name, file_content in files:
            output.write(f"M 100644 {file_name}\n")  # File mode and name
            output.write(f"data {len(file_content)}\n")  # File content length
            output.write(f"{file_content}\n")  # File content
            output.write(f"###\n")

# Import the fast-import data into the Git repository
subprocess.run(["git", "fast-import", "<", "synergy-to-git.import"])

# Add all changes to Git
subprocess.run(["git", "add", "."])

# Commit the changes
subprocess.run(["git", "commit", "-m", "Migrated from Synergy"])

# Push to GitHub (replace the URL with your GitHub repo URL)
subprocess.run(["git", "push", "-u", "origin", "master"])
