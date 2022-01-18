#!/usr/bin/env python3.10


import json
import sys
from time import sleep
import github


SECONDS_BETWEEN_REQUESTS = 3


def main():
    token, repo_name, issuefile = sys.argv[1:4]
    github_ = github.Github(token, )
    repo = get_repo(github_, repo_name)
    issues = load_json_file(issuefile)
    labels = repo.get_labels()
    label_map = create_label_map(labels)
    load_issues(repo, issues, label_map)


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


def create_label_map(labels):
    m = {}
    for label in labels:
        m[label.name] = label
    return m


def load_issues(repo, issues, label_map):
    for issue in issues:
        labels = [label_map[label_name] for label_name in issue['labels']]
        print(f'Loading issue: {issue["title"]}')
        repo.create_issue(issue['title'], body=issue['body'], labels=labels)
        sleep(SECONDS_BETWEEN_REQUESTS)


if __name__ == '__main__':
    main()
