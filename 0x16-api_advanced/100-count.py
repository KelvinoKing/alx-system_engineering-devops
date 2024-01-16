#!/usr/bin/python3
"""
import requests module
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    parses the title of all hot articles, and prints a sorted count
    of given keywords
    """
    if word_counts is None:
        word_counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    headers = {'User-Agent': 'your_user_agent_here'}

    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])

            if not children:
                # No more articles found
                print_results(word_counts)
                return

            for child in children:
                title = child.get('data', {}).get('title', '').lower()
                count_keywords(title, word_list, word_counts)

            after = data.get('data', {}).get('after', None)

            # Recursive call to get the next page of results
            count_words(subreddit, word_list, after, word_counts)
        elif response.status_code == 404:
            # Invalid subreddit
            return
        else:
            return
    except Exception as e:
        return


def count_keywords(title, word_list, word_counts):
    for keyword in word_list:
        keyword_lower = keyword.lower()

        if keyword_lower in title:
            word_counts[keyword_lower] = word_counts.get(
                    keyword_lower, 0) + title.count(keyword_lower)


def print_results(word_counts):
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
