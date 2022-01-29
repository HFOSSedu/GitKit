# Kit - User Guide

## `create_instance.py`

### Overview of `create_instance.py`

`create_instance.py` creates an independent instance of a kit environment. In particular, it creates a repository on GitHub in the organization or under your account, and with the name you specify. It loads this repository with the contents of this project's main branch, and some predefined issues and labels given in JSON files in this project's Instructor branch (see .kit/data).

### Install dependencies for `create_instance.py`

There are two ways to run `create_instance.py`: natively or using a development container. To run it natively, you need first install the following dependencies.

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

### Use `create_instance.py`

1. [Generate an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
    - In **Note** name your token based on the instance you are creating. For example, if you are creating a Kit instance for cs101, name it cs101.
    - We recommend specifying an **Expiration** for the token, and naming it based on the instance you are creating.
    - Under **Select scopes**, select **repo** and **workflow**, and leave the others unselected.
    - **Anyone with this token can manipulate your repositories on GitHub.** Keep this token safe, and expire it when you no longer need it (you can always get another). This token will be saved in the URL for the `kit_instance` remote in your in your local git files (.git) but are not stored in the repository data itself. The token is saved in plain text.

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

4. If not yet running (look for the Docker Whale in your system tray or use the command line to [Check whether Docker is running](https://docs.docker.com/config/daemon/#check-whether-docker-is-running)), start Docker and wait for it to be ready.

5. Open the root of the project in VS Code. If you have VS Code installed in your system's path (see VS Code install instructions for [Windows](https://code.visualstudio.com/docs/setup/windows), [macOS](https://code.visualstudio.com/docs/setup/mac), and [Linux](https://code.visualstudio.com/docs/setup/linux)), this can be done with the following command (the dot at the end of the line in the following instruction is intentional and important; it represents the current directory).

        ```bash
        code .
        ```

> **TIP:** If VS Code asks you to install Python, you can ignore this because the development container will do this for you.

6. When VS Code asks if you would like to "reopen in container", do so. If you miss it, click the `><` in the lower left corner and select the "reopen in container".

7. Start a terminal in VS Code; one way to do this is to press CTRL+`  (the grave accent key; usually it's left of the 1-key).

8. Run create_instance.py

    ```bash
    .kit/bin/create_instance.py YOUR_TOKEN [ORG/]REPO
    ```

    Where YOUR_TOKEN is the token you generated in GitHub in the first step, ORG is the name of the organization or your login name which will contain the new repository, and REPO is the name you would like for the new repository. ORG is optional (thus the square brackets; do not type the square brackets). If you do provide an ORG, you must separate it from the REPO with a `/`. For example `HFOSSedu/my_new_repository`. If you do not provide an ORG, the new repository will be created under your login.

    This will take several minutes to complete. When done your new repository will have been created and will contain the issues, labels, and source code necessary to complete the activities in this kit.  Your local repository will have a new remote named kit_instance. The URL in this remote contains the token. Keep this token confidential. Anyone who has it can manipulate your repositories on GitHub.

## Claiming issues in the instance

Anyone can claim an issue by leaving the following comment:

    I would like to work on this please!


# Kit - Developer Guide

## Manage Python Dependencies

```
cd .kit
pipenv install --system SPLAT
pipenv install --system --dev SPLAT
pipenv lock -r > requirements.txt
pip install requirements.txt
```
