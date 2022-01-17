#!/usr/bin/env bash

# usage: cat issues.json | process-issues.bash > issues-processed.json

jq '[.[] | {name, description, color}]'
