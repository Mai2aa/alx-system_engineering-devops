#!/usr/bin/python3
""" How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers 
    including : Non-Active users"""
    try:
        headers = {'User-Agent': 'MyRedditApp/1.0 by /u/Mai2aa'}
        response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers=headers)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except:
        return 0