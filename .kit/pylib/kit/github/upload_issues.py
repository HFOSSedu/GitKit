from kit import command_line
from kit import github
from kit import json


def main():
    token, repo_name, issues_filename = command_line.get_args(3)
    connection = github.connect(token)
    repo = github.get_repo(connection, repo_name)
    issues = json.load_file(issues_filename)
    labels = github.get_labels(repo)
    labels_by_name = to_labels_by_name(labels)
    upload_issues(repo, issues, labels_by_name)


def to_labels_by_name(labels):
    m = {}
    for label in labels:
        m[label.name] = label
    return m


def upload_issues(repo, issues, label_by_name):
    for issue in issues:
        labels = [label_by_name[label_name] for label_name in issue['labels']]
        repo.create_issue(issue['title'], body=issue['body'], labels=labels)
        github.delay_after_notification()
        print(f'Uploaded issue: {issue["title"]}')


if __name__ == '__main__':
    main()
