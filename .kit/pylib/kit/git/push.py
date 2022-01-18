import git


def push(remote, branch_name):
    remote.push(branch_name, progress=MyProgressPrinter()).raise_if_error()


class MyProgressPrinter(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        percent_done = str(round((cur_count / (max_count or 100.0))*100, 1)) + '%'
        print("Pushing main", percent_done, message)
