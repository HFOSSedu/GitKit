#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${SCRIPT_DIR}"

## Install git hooks
cp .hooks/pre-commit ../.git/hooks/pre-commit
cp .hooks/pre-merge-commit ../.git/hooks/pre-merge-commit
cp .hooks/pre-rebase ../.git/hooks/pre-rebase
git config branch.main.mergeoptions "--no-ff"

## Check origin remote URL does not contain upstream's name.
source ./env
ORIGIN="$(git remote -v | grep origin)"
if [[ "$ORIGIN" == *"$KIT_UPSTREAM_NAME"* ]] ; then
    echo "*********************************************************************"
    printf "\xF0\x9F\x98\xBA Meow, Kitty here!\n"
    echo
    echo "Oops, I think you have cloned the upstream repository instead of your"
    echo "fork. But don't worry. You can fix it!"
    echo
    echo "1. Delete your local repository."
    echo "2. Navigate to your fork on GitHub and copy its clone URL."
    echo "3. Clone your fork using its clone URL."
    echo "*********************************************************************"
fi
