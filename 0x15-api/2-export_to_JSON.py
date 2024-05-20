#!/usr/bin/python3
""" Export api to csv"""
import json
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    dict_users = {user: []}
    for task in tasks:
        completed = task.get('completed')
        title_task = task.get('title')
        dict_users[user].append({
            "task": task,
            "completed": completed,
            "username": user_name})
    with open('{}.json'.format(user), 'w') as jsonfile:
        json.dump(dict_users, jsonfile)
