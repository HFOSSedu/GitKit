from kit import github


def get_namespace(connection, user, repo_name):
    full_name = github.to_full_repo_name(user.login, repo_name)
    parts = full_name.split('/')
    if parts[0] == user.login:
        return user
    else:
        return github.get_org(connection, parts[0])
