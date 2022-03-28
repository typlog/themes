import re
import sys
import json
from urllib.request import Request, urlopen


LINK_ANCHOR = re.compile(r'<a[^>]+><svg class="octicon octicon-link".+?</svg></a>')
url_base = 'https://api.github.com/repos/'


def fetch_theme_info(repo):
    url = f'https://raw.githubusercontent.com/{repo}/master/theme.json'
    req = Request(url)
    with urlopen(req) as f:
        return json.load(f)


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
    return LINK_ANCHOR.sub('', content)


def update_theme(name, repo):
    data = fetch_theme_info(repo)
    print('update:', name, repo, data['version'])
    info = fetch_repo_data(repo)
    data['id'] = name
    data['avatar'] = info['owner']['avatar_url']
    data['stars'] = info['watchers']
    data['readme'] = fetch_readme(repo)
    with open(f'data/{name}.json', 'w') as f:
        json.dump(data, f)


def main():
    with open('registry.json') as f:
        data = json.load(f)
        for name in data:
            update_theme(name, data[name])


if __name__ == '__main__':
    main()
