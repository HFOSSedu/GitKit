#!/usr/bin/env python3.10


import json
import sys
from time import sleep
import github


def main():
    token, repo_name, filename = sys.argv[1:4]
    github_ = github.Github(token)
    repo = get_repo(github_, repo_name)
    labels = load_json_file(filename)
    load_labels(repo, labels)


def get_repo(github_, repo_name):
    login = github_.get_user().login
    full_repo_name = to_full_repo_name(login, repo_name)
    repo = github_.get_repo(full_repo_name)
    return repo


def to_full_repo_name(user_name, repo_name):
    return repo_name if '/' in repo_name else f'{user_name}/{repo_name}'


def load_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def load_labels(repo, labels):
    for label in labels:
        print(f'Loading label: {label["name"]}')
        repo.create_label(label['name'], label['color'], label['description'])
        sleep(1)


if __name__ == '__main__':
    main()
