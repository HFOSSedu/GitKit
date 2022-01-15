def to_full_repo_name(user_name, repo_name):
    return repo_name if '/' in repo_name else f'{user_name}/{repo_name}'
