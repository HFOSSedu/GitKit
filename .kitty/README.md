# Kitty

This file: .kitty/README.md

## Dependencies

* Bash
* Python 3.6+

## Install

This must be done once after cloning.

In git-bash (Windows), bash (Linux), zsh (Mac Terminal) run

```bash
.kitty/init
```

## Design

These changes must exist in GitKit's main branch, not the instructor.

`.kitty/init`

* Checks that origin is not upstream.
* Checks that upstream is not a fork (and is therefore is the upstream).
* Install git hooks (copy or link from .kitty/hooks to .git/hooks)

`.kitty/hooks/*`

* A hook will check for and prevent commits to main.
* A hook will check for and prevent merges to main.
* A hook will check for and prevent rebases to main.


## TODO

* See how `.kitty/init` interacts with DevContainer (if a DevContainer is used).


## Resources

* https://gist.github.com/aaronhoffman/ffbfd36928f9336be2436cffe39feaec
* https://gist.github.com/ilyakatz/4625224#file-pre-commit-master-no-no
* https://githooks.com/

