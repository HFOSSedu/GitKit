#!/usr/bin/env python3.10
'''
save_issues.py
'''

import json
from pathlib import Path
import sys


import github
import git


def main():
    token, org_name, repo_name = get_command_line_params()
    save_issues(token, org_name, repo_name)


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


def save_issues(token, org_name, repo_name):
    g = github.Github(token)
    repo = g.get_repo(f"{org_name}/{repo_name}")
    open_issues = repo.get_issues(state='open')
    issues = []
    for issue in open_issues:
        issues.append(issue._rawData)
    print(json.dumps(issues, indent=4))


if __name__ == '__main__':
    main()
