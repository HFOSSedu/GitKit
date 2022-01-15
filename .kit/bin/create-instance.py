#!/usr/bin/env python3.10
import os
import sys
import pathlib

import github


def main():
    token, full_repo_name = get_params()
    api_repo = create_empty_repository_on_github(token, full_repo_name)
    


def get_params():
    return sys.argv[1:]


def create_empty_repository_on_github(token, full_repo_name):
    parts = full_repo_name.split('/')
    if len(parts) == 1:
        g = github.Github(token)
        u = g.get_user()
        return u.create_repo(parts[0])
    else:
        g = github.Github(token)
        u = g.get_user()
        o = get_org_by_login(u, parts[0])
        return o.create_repo(parts[1])


def get_org_by_login(user, org_name):
    orgs = user.get_orgs()
    for o in orgs:
        if o.login.lower() == org_name:
            return o
    raise Exception(f'You are not a member of {org_name}.')



if __name__ == '__main__':
    main()
