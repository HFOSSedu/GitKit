#!/usr/bin/env python3.10
'''
get_labels.py
'''

import json
from pathlib import Path
import sys


import github
import git


def main():
    token, org_name, repo_name = get_command_line_params()
    get_labels(token, org_name, repo_name)


def get_command_line_params():
    cl = CommandLine()
    token = cl.get_token()
    org_name = cl.get_org_name()
    repo_name = cl.get_repo_name()
    return token, org_name, repo_name


class CommandLine:
    def get_token(self):
        return sys.argv[1]

    def get_org_name(self):
        parts = self._get_repo_name_parts()
        return None if len(parts) == 1 else parts[0]

    def get_repo_name(self):
        parts = self._get_repo_name_parts()
        return parts[0] if len(parts) == 1 else parts[1]

    def _get_repo_name_parts(self):
        return sys.argv[2].split('/')


def get_labels(token, org_name, repo_name):
    g = github.Github(token)
    repo = g.get_repo(f"{org_name}/{repo_name}")
    labels = []
    for label in repo.get_labels():
        labels.append(label._rawData)
    print(json.dumps(labels, indent=4))


if __name__ == '__main__':
    main()
