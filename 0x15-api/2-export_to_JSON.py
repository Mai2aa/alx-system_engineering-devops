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

    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name
        })

    output = {user: user_tasks}
    with open('{}.json'.format(user), 'w') as jsonfile:
        json.dump(output, jsonfile)
