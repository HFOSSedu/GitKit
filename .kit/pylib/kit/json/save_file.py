import json


def save_file(python_json, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(python_json, f, indent=4)
