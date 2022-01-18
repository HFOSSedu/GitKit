#!/usr/bin/env python3.10
'''
create_instance.py
'''


from pathlib import Path
import sys


import github
import git


def main():
    token, org_name, repo_name = get_command_line_params()
    create_instance_repo(token, org_name, repo_name)


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


def create_instance_repo(token, org_name, repo_name):
    InstanceCreator().create_instance(token, org_name, repo_name)


class InstanceCreator:
    def __init__(self):
        self.token = None
        self.github = None
        self.username = None
        self.instance_repo = None
        self.local_repo = None
        self.progress_monitor = MyProgressPrinter()

    def create_instance(self, token, org_name, repo_name):
        self.connect_to_github(token)
        self.create_empty_instance_repo(org_name, repo_name)
        self.create_instance_remote()
        self.push_main_to_instance_repo()
        delete_all_issues(self.github, repo_name)

    def connect_to_github(self, token):
        self.token = token
        self.github = github.Github(self.token)
        self.username = self.github.get_user().login

    def create_empty_instance_repo(self, org_name, repo_name):
        self.instance_repo = create_empty_repository(self.github, org_name, repo_name)

    def create_instance_remote(self):
        local_repo = self.get_local_repo()
        auth_url = self.get_authorized_clone_url()
        local_repo.create_remote('instance', auth_url)
        return local_repo.remote('instance')

    def get_local_repo(self):
        if self.local_repo is None:
            self.local_repo = get_local_repo()
        return self.local_repo

    def get_authorized_clone_url(self):
        return self.instance_repo.clone_url.replace('https://', f'https://{self.username}:{self.token}@')

    def push_main_to_instance_repo(self):
        self.get_local_repo().remote('instance').push('main', progress=self.progress_monitor).raise_if_error()


class MyProgressPrinter(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        percent_done = round((cur_count / (max_count or 100.0))*100, 1) + '%'
        print("Pushing main", percent_done, message)


def get_local_repo():
    d = Path(__file__).parent
    while not contains_git_dir(d):
        d = d.parent
    return git.Repo(d)


def contains_git_dir(d):
    subds = [subd for subd in d.iterdir() if subd.is_dir()]
    for subd in subds:
        if subd.name == '.git':
            return True
    return False


def create_empty_repository(gh, org_name, repo_name):
    erc = EmptyRepositoryCreator(gh)
    erc.create(org_name, repo_name)
    return erc.repo


class EmptyRepositoryCreator:
    def __init__(self, github_):
        self.github = github_
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


def delete_all_issues(gh, repo_name):
    full_name = to_full_name(gh.get_user().login, repo_name)
    repo = gh.get_repo(full_name)
    for i in repo.get_issues():
        i.delete()


def to_full_name(user_name, repo_name):
    return repo_name if '/' in repo_name else f'{user_name}/{repo_name}'


if __name__ == '__main__':
    main()
