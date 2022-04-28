import os
import json
from collections import OrderedDict


def normalize(data):
    rv = {}
    keys = ['id', 'name', 'name#ja', 'images', 'stars', 'tags']
    for k in keys:
        rv[k] = data.get(k)
    return rv


def run():
    data = []
    mapping = {}

    with open('registry.json') as f:
        registry = json.load(f, object_pairs_hook=OrderedDict)

    for name in registry:
        filepath = os.path.join('data', name + '.json')
        with open(filepath) as f:
            theme = json.load(f)
            data.append(normalize(theme))

            repo = theme['repo']
            version = theme.get('version')
            if version:
                repo = f'{repo}@{version}'
            mapping[name] = repo

    with open('index.json', 'w') as f:
        json.dump(data, f)

    with open('names.json', 'w') as f:
        json.dump(mapping, f)


if __name__ == '__main__':
    run()
