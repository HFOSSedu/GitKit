from pathlib import Path


DELAY_SECONDS_AFTER_GITHUB_READS=1
DELAY_SECONDS_AFTER_GITHUB_WRITES=1
DELAY_SECONDS_AFTER_GITHUB_NOTIFICATION=3
KIT_DATA_DIR=Path(__file__).parent.parent.parent / 'data'
ISSUES_FILE=KIT_DATA_DIR / 'issues-processed.json'
LABELS_FILE=KIT_DATA_DIR / 'labels-processed.json'
