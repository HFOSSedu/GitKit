#!/usr/bin/env python3.10
'''
create-instance.py
'''

import sys


import github


def main():
    cl = CommandLine()
    gh = github.Github(cl.get_token())
    erc = EmptyRepositoryCreator(gh)
    erc.create(cl.get_org_name(), cl.get_repo_name())


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


class EmptyRepositoryCreator:
    def __init__(self, github):
        self.github = github
        self.repo = None

    def create(self, org_name, repo_name):
        namespace = self._get_namespace(org_name)
        self.repo = namespace.create_repo(repo_name)

    def _get_namespace(self, org_name):
        u = self.github.get_user()
        return u if org_name is None else self._get_org(u, org_name)

    def _get_org(self, user, org_name):
        for o in user.get_orgs():
            if o.login.lower() == org_name:
                return o
        raise Exception(f'You are not a member of {org_name}.')


if __name__ == '__main__':
    main()
