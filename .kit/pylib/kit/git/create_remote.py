def create_remote(local_repo, remote_name, remote_url):
    local_repo.create_remote(remote_name, remote_url)
    return local_repo.remote(remote_name)
