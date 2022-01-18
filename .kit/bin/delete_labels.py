#!/usr/bin/env python3.10


import sys
from time import sleep
import github


def main():
    token, repo_name = sys.argv[1:3]
    github_ = github.Github(token)
    login = github_.get_user().login
    full_repo_name = to_full_repo_name(login, repo_name)
    repo = github_.get_repo(full_repo_name)
    delete_all_labels(repo)


def to_full_repo_name(user_name, repo_name):
    return repo_name if '/' in repo_name else f'{user_name}/{repo_name}'


def delete_all_labels(repo):
    for label in repo.get_labels():
        print(f'Deleting label: {label.name}')
        label.delete()
        sleep(1)


if __name__ == '__main__':
    main()
