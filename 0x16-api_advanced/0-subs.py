#!/usr/bin/python3
"""import request module
"""
import requests


def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API and
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """

    headers = {'User-Agent': 'VirboxBot'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            subreddit_info = response.json()

            return subreddit_info['data']['subscribers']
        else:
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
