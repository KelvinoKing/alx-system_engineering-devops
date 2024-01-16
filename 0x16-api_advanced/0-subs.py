#!/usr/bin/python3
"""import request module
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a subreddit
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        subscribers = data['data']['subscribers']

        return subscribers
    except requests.exceptions.RequestException:
        return 0
    except KeyError:
        return 0
