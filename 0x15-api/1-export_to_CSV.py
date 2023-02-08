#!/usr/bin/python3
"""Export data about a user and tasks to csv"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    resp = requests.get(url)
    tasks = resp.json()
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    resp = requests.get(url)
    user = resp.json()

    user_id = str(argv[1])
    username = user.get("username")

    with open(user_id + ".csv", "w") as f:
        for task in tasks:
            completed = task.get("completed")
            text = task.get("title")
            line = '"{}","{}","{}","{}"\n'.format(user_id,
                                                  username,
                                                  completed,
                                                  text)
            f.write(line)
