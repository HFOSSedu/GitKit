# Kit - User Guide

## `create-instance.py`

### Overview of `create-instance.py`

`create-instance.py` creates an independent instance of a kit environment. In particular, it creates a repository on GitHub in the organization or under your account, and with the name you specify. It loads this repository with the contents of this project's main branch, and some predefined issues and labels given in JSON files in this project's Instructor branch (see .kit/data).

### Install dependencies for `create-instance.py`

There are two ways to run `create-instance.py`: natively or using a development container. To run it natively, you need first install the following dependencies.

* [Git 2.34](https://git-scm.com/)
* [Python 3.10](https://www.python.org/)
* [PyGitHub 1.55](https://pygithub.readthedocs.io/en/latest/introduction.html)
* [GitPython 3.1](https://gitpython.readthedocs.io/en/stable/)

Alternatively, if you would rather use a development container, don't install the above dependencies. Instead, install the following dependencies.

* [Git 2.34](https://git-scm.com/)
* [Docker](https://www.docker.com/get-started)
* [VS Code](https://code.visualstudio.com/)
* [Remote - Containers Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

What's the difference? A development container is an isolated environment that contains the first set of dependencies pre-installed. That means there is little risk of the development container to interfere with the dependencies of any other software you have installed or will install on your computer. Also, it ensures that you have the exact versions of the dependencies that the developers wrote and tested against. The disadvantage is that it relies on Docker which requires a minimum of 4GB RAM to run, and really 8GB+ to run comfortably.

### Use `create-instance.py`

1. [Generate an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with privileges over your repositories. We recommend specifying a timeout for the token, and naming it based on the instance you are creating. This token will be used to create your new repository and will be saved in the clear in remote named kit_instance in your local repository. Keep this token safe, and expire it when you no longer need it (you can always get another). Anyone who has it can use it to manipulate your repositories on GitHub.

2. Clone GitKit and change to the directory it creates. In this example we are cloning it into cs101.

    ```bash
    git clone https://github.com/HFOSSedu/GitKit.git cs101
    cd cs101
    ```

> **NOTE:** You'll need a separate clone for each instance you plan to deploy. Your local clone will become your instructor control for the instance.

3.  Switch to the Instructor branch.

    ```bash
    git switch Instructor
    ```

> **NOTE:** If you are not using the devcontainer, you can skip ahead to step 8.

4. If not yet running, start Docker and wait for it to be ready.

5. Start VS Code (the dot at the end of the line in the following instruction is intentional and important; it represents the current directory).

    ```bash
    code .
    ```

6. When VS Code asks if you would like to "reopen in container", do so. If you miss it, click the `><` in the lower left corner and select the "reopen in container".

7. Start a terminal in VS Code; one way to do this is to press CTRL+`  (the grave accent key; usually it's left of the 1-key).

8. Run create-instance.py

    ```bash
    .kit/bin/create-instance.py YOUR_TOKEN [ORG/]REPO
    ```

    Where YOUR_TOKEN is the token you generated in GitHub in the first step, ORG is the name of the organization or your login name which will contain the new repository, and REPO is the name you would like for the new repository. ORG is optional (thus the square brackets; do not type the square brackets). If you do provide an ORG, you must separate it from the REPO with a `/`. For example `HFOSSedu/my_new_repository`. If you do not provide an ORG, the new repository will be created under your login.

    This will take several minutes to complete. When done your new repository will have been created and will contain the issues, labels, and source code necessary to complete the activities in this kit.  Your local repository will have a new remote named kit_instance. The URL in this remote contains the token. Keep this token confidential. Anyone who has it can manipulate your repositories on GitHub.

# Kit - Developer Guide

## Manage Python Dependencies

```
cd .kit
pipenv install --system SPLAT
pipenv install --system --dev SPLAT
pipenv lock -r > requirements.txt
pip install requirements.txt
```
