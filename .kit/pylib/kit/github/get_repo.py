from kit import github


def get_repo(connection, repo_name):
    login = github.get_authenticated_user(connection).login
    full_repo_name = github.to_full_repo_name(login, repo_name)
    repo = connection.get_repo(full_repo_name)
    github.delay_after_read()
    print(f'Fetched repository {repo.name}')
    return repo
