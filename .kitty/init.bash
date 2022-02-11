#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${SCRIPT_DIR}"

# Install git hooks
cp .hooks/pre-commit ../.git/hooks/pre-commit
cp .hooks/pre-commit ../.git/hooks/pre-merge-commit
cp .hooks/pre-rebase ../.git/hooks/pre-rebase
