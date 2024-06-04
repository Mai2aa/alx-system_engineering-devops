#!/usr/bin/python3
""" How many subs?"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers
    including : Non-Active users"""
    try:
        headers = {'User-Agent': 'My-User-Agent'}
        response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers=headers,
            allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except (requests.exceptions.RequestException, KeyError):
        return 0
