import pathlib
from kit import github
from kit import json
from kit import git
from kit import config


def create_instance(token, user, repo_desc, remote_name='kit_instance', labels_file=config.LABELS_FILE, issues_file=config.ISSUES_FILE):
    label_data = json.load_file(labels_file)
    issue_data = json.load_file(issues_file)

    local_repo = git.get_local_repo()

    # Ensure main exists locally.
    active_branch = local_repo.active_branch
    origin = local_repo.remotes.origin
    local_repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()

    # Commit upstream name to main
    env_file = pathlib.Path(local_repo.working_tree_dir) / '.kitty' / 'env'
    with open(env_file, 'w') as f:
        f.write(f'KIT_UPSTREAM_NAME="{str(repo_desc)}"')
    local_repo.index.add([env_file])
    local_repo.index.commit('kit: add upstream repository name')
    active_branch.checkout()

    # Create repository on GitHub.
    repo = repo_desc.create_empty_repo()

    # Push main to GitHub.
    authorizing_clone_url = git.add_authorization_to_clone_url(repo.clone_url, user.login, token)
    remote = git.create_remote(local_repo, remote_name, authorizing_clone_url)
    git.push(remote, 'main')

    # Synchronize labels.
    github.delete_all_labels(repo)
    github.upload_labels(repo, label_data)

    # Upload issues.
    labels = github.get_labels(repo)
    labels_by_name = github.to_labels_by_name(labels)
    github.upload_issues(repo, issue_data, labels_by_name)

