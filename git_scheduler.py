import subprocess
# import os
import sys

# This function is used to push the changes to remote repo
def git_push(git_directory):
    subprocess.run(['git', '-C', git_directory, 'push'])
    print("Changes pushed succesfully")
    # sys.stdout.write("Changes pushed succesfully")


# This function is used to stage the changes which are mentioned in the file
def git_add(git_directory, file_path):
    print(git_directory)
    print(file_path)
    subprocess.run(['git', '-C', git_directory, 'add', file_path])
    print("File added succesfully")


# This function is used to commit in the local-repo
def git_commit(git_directory, commit_msg):
    subprocess.run(['git', '-C', git_directory, 'commit', '-m', f"{commit_msg}"])
    print("Changes commited succesfully")


def git_all(git_directory, file_path, commit_msg):
    git_add(git_directory, file_path)
    git_commit(git_directory, commit_msg)
    git_push(git_directory)
    print("All git process done")
    return

