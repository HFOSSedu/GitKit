from kit import github


def get_open_issues(repo):
    issues = []
    for issue in repo.get_issues():
        issues.append(issue)
        github.delay_after_read()
        print(f'Fetched issue #{issue.number}')
    return issues
