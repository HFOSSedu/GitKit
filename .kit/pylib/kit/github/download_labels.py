from kit import command_line
from kit import github
from kit import json


def main():
    token, repo_name, labels_filename = command_line.get_args(3)
    connection = github.connect(token)
    repo = github.get_repo(connection, repo_name)
    download_labels(repo, labels_filename)


def download_labels(repo, labels_filename):
    labels = github.get_labels(repo)
    labels_json = github.to_json(labels)
    json.save_file(labels_json, labels_filename)
    print(f'Labels saved to {labels_filename}')


if __name__ == '__main__':
    main()
