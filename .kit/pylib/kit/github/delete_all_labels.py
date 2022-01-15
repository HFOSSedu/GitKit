from kit import command_line
from kit import github


def main():
    token, repo_name = command_line.get_args(2)
    connection = github.connect(token)
    repo = github.get_repo(connection, repo_name)
    delete_all_labels(repo)


def delete_all_labels(repo):
    for label in repo.get_labels():
        github.delay_after_read()
        label.delete()
        github.delay_after_write()
        print(f'Deleted label {label.name}')


if __name__ == '__main__':
    main()
