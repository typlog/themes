import re
import sys
import json
from urllib.request import Request, urlopen


LINK_ANCHOR = re.compile(r'<a[^>]+><svg class="octicon octicon-link".+?</svg></a>')
url_base = 'https://api.github.com/repos/'


def fetch_repo_data(repo):
    url = f'{url_base}{repo}'
    req = Request(url)
    req.add_header('Accept', 'application/json')
    # req.add_header('Authorization', 'Bearer')
    with urlopen(req) as f:
        return json.load(f)


def fetch_readme(repo):
    url = f'{url_base}{repo}/readme'
    req = Request(url)
    req.add_header('Accept', 'application/vnd.github.html')
    # req.add_header('Authorization', 'Bearer')
    with urlopen(req) as f:
        content = f.read()
    content = content.decode('utf-8')
    return LINK_ANCHOR.sub('</a>', content)


def update_theme(name):
    with open(f'registry/{name}') as f:
        data = json.load(f)

    repo = data['repo']
    info = fetch_repo_data(repo)
    data['avatar'] = info['owner']['avatar_url']
    data['stars'] = info['watchers']
    data['readme'] = fetch_readme(repo)
    with open(f'data/{name}', 'w') as f:
        json.dump(data, f)


def main():
    filenames = sys.argv[1:]
    for filename in filenames:
        if filename.startswith('registry/'):
            name = filename.split('/', 1)[1]
            try:
                print('update:', name)
                update_theme(name)
            except Exception as error:
                print('failed:', error)


if __name__ == '__main__':
    main()
