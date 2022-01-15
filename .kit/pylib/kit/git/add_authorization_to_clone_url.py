def add_authorization_to_clone_url(clone_url, login, token):
    return clone_url.replace('https://', f'https://{login}:{token}@')
