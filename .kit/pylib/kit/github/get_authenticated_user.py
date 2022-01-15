from kit import github


def get_authenticated_user(connection):
    u = connection.get_user()
    github.delay_after_read()
    print(f'Fetched authenticated user {u.login}')
    return u
