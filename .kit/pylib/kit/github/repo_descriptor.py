from kit import github


class RepoDescriptor:
    def __init__(self, connection, user, repo_name):
        parts = repo_name.split('/')
        if len(parts) == 1:
            self.namespace_name = user.login
            self.namespace = user
            self.repo_name = repo_name
        elif parts[0] == user.login:
            self.namespace_name = user.login
            self.namespace = user
            self.repo_name = parts[1]
        else:
            self.namespace_name = parts[0]
            self.namespace = github.get_org(connection, parts[0])
            self.repo_name = parts[1]

    def create_empty_repo(self):
        repo = self.namespace.create_repo(self.repo_name)
        github.delay_after_notification()
        print(f'Created empty repo {repo.url}')
        return repo
