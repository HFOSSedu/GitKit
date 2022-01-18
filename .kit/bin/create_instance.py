#!/usr/bin/env python3.10

import sys
import pathlib
path_to_kits_python_libraries = str((pathlib.Path(__file__).parent.parent / 'pylib').absolute())
sys.path.append(path_to_kits_python_libraries)

from kit.create_instance import create_instance
from kit import command_line
from kit import github


token, repo_name = command_line.get_args(2)
connection = github.connect(token)
user = github.get_authenticated_user(connection)
repo_desc = github.RepoDescriptor(token, user, repo_name)
create_instance(token, user, repo_desc)
