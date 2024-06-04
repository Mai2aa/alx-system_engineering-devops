#!/usr/bin/python3
"""Module 1-top_ten"""
import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEAD = {'User-Agent': 'Hi/0.'}
    response = requests.get(URL, headers=HEAD)
    if response.status_code == 200:
        data = response.json().get('data')
        [print(child["data"]["title"]) for child in data["children"]]
        return
    print('None')