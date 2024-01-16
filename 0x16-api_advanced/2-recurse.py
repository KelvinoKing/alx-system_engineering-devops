#!/usr/bin/python3
"""
import requests module
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    queries the Reddit Api and returns a list containing the titles of
    all hot articles for a given subreddit
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Kelvino'}

    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])

            if not children:
                if not hot_list:
                    return None
                else:
                    return hot_list

            for child in children:
                title = child.get('data', {}).get('title', '')
                hot_list.append(title)

            after = data.get('data', {}).get('after', None)

            return recurse(subreddit, hot_list, after)

        if response.status_coe == 404:
            return None
        else:
            return None
    except Exception:
        return None
