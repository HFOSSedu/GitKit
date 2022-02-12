#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${SCRIPT_DIR}"

# Install git hooks
# cp .hooks/pre-commit ../.git/hooks/pre-commit
# cp .hooks/pre-merge-commit ../.git/hooks/pre-merge-commit
# cp .hooks/pre-rebase ../.git/hooks/pre-rebase
# git config branch.main.mergeoptions "--no-ff"

# Load environment variables including KIT_UPSTREAM_NAME
source ./env
ORIGIN="$(git remote -v | grep origin)"
if [[ "$ORIGIN" == *"$KIT_UPSTREAM_NAME"* ]] ; then
    echo "*********************************************************************"
    printf "\xF0\x9F\x98\xBA Meow, Kitty here!\n"
    echo
    echo "Oops, I think you have cloned the upstream repository instead of your"
    echo "fork. Use the following command below to inspect your local"
    echo "repository's remotes."
    echo
    echo "    git remote -v"
    echo
    echo "Look for the 'origin' remote. If its URL points to upstream and not"
    echo "your fork, you have a problem. But don't worry. You can fix it!"
    echo "You'll need to delete your local repository, then navigate to your"
    echo "fork on GitHub, copy its clone URL, and then try clone using that"
    echo "URL. Don't forget to initialize me again so I can help out."
    echo "*********************************************************************"
fi
