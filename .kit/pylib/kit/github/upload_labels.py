from kit import command_line
from kit import github
from kit import json


def main():
    token, repo_name, labels_filename = command_line.get_args(3)
    connection = github.connect(token)
    repo = github.get_repo(connection, repo_name)
    labels = json.load_file(labels_filename)
    upload_labels(repo, labels)


def upload_labels(repo, labels):
    for label in labels:
        repo.create_label(label['name'], label['color'], label['description'])
        github.delay_after_write()
        print(f'Uploaded label: {label["name"]}')


if __name__ == '__main__':
    main()
