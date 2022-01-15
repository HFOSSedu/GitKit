#!/usr/bin/env bash

# usage: cat issues.json | process-issues.bash > issues-processed.json

jq '[.[] | {title, body, labels: [.labels[] | .name]}]'
