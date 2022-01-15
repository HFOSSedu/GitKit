from kit import github
from kit import json
from kit import git
from kit import config


def create_instance(token, user, repo_desc, remote_name='kit_instance', main_branch_name='main', labels_file=config.LABELS_FILE, issues_file=config.ISSUES_FILE):
    label_data = json.load_file(labels_file)
    issue_data = json.load_file(issues_file)

    repo = repo_desc.create_empty_repo()
    github.delete_all_labels(repo)
    github.upload_labels(repo, label_data)
    labels = github.get_labels(repo)
    labels_by_name = github.to_labels_by_name(labels)
    github.upload_issues(repo, issue_data, labels_by_name)

    authorizing_clone_url = git.add_authorization_to_clone_url(repo.clone_url, user.login, token)
    local_repo = git.get_local_repo()
    remote = git.create_remote(local_repo, remote_name, authorizing_clone_url)
    git.push(remote, main_branch_name)
