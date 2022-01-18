from kit import github


def get_labels(repo):
    labels = []
    for label in repo.get_labels():
        labels.append(label)
        github.delay_after_read()
        print(f'Fetched label {label.name}')
    return labels
