#!/usr/bin/python3
"""handle requests"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    if not subreddit or type(subreddit) is not str:
        return 0
    URL = f"https://www.reddit.com/r/{subreddit}/about/"
    HEAD = {'User-Agent': 'Hi/0.0'}

    response = requests.get(URL, headers=HEAD)
    if response.status_code == 200:
        data = response.json()
    else:
        return 0
    return data['data']['subscribers']
