import github


def connect(token):
    return github.Github(token)
