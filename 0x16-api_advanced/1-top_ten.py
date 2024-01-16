#!/usr/bin/python3
"""import requests module
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    headers = {'User-Agent': 'Kelvino'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)

    except Exception as e:
        print(None)
