import os
import json


def normalize(data):
    if 'readme' in data:
        del data['readme']
    return data


def run():
    data = []
    mapping = {}

    names = os.listdir('data')
    for name in names:
        if name.endswith('.json'):
            filepath = os.path.join('data', name)
            with open(filepath) as f:
                theme = json.load(f)
                data.append(normalize(theme))
                mapping[name[:-5]] = theme['repo']

    with open('index.json', 'w') as f:
        json.dump(data, f)

    with open('mapping.json', 'w') as f:
        json.dump(mapping, f)


if __name__ == '__main__':
    run()
