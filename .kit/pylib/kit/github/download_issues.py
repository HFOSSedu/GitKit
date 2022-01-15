from kit import command_line
from kit import github
from kit import json


def main():
    token, repo_name, issues_filename = command_line.get_args(3)
    connection = github.connect(token)
    repo = github.get_repo(connection, repo_name)
    download_issues(repo, issues_filename)


def download_issues(repo, issues_filename):
    issues = github.get_open_issues(repo)
    issues_json = github.to_json(issues)
    json.save_file(issues_json, issues_filename)
    print(f'Issues saved to {issues_filename}')


if __name__ == '__main__':
    main()
