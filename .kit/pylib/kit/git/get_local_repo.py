from pathlib import Path
import git


def get_local_repo():
    directory = Path(__file__).parent
    while not is_project_root(directory):
        directory = directory.parent
    return git.Repo(directory)


def is_project_root(directory):
    return '.git' in directory_names(directory)


def directory_names(directory):
    for file in directory.iterdir():
        if file.is_dir():
            yield file.name
