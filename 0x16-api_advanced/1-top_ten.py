#!/usr/bin/python3
"""import requests module
"""

import requests


def top_ten(subreddit):
    """Prints 10 post's titles
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Kelvino'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
    except KeyError:
        print("None")
