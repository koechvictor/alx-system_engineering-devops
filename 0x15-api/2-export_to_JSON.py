#!/usr/bin/python3
"""Export data about a user and tasks to json"""
import json
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

    new_tasks = []
    new_task = {}
    for task in tasks:
        new_task["task"] = task.get("title")
        new_task["completed"] = task.get("completed")
        new_task["username"] = username
        new_tasks.append(new_task)
        new_task = {}

    my_json = {}
    my_json[user_id] = new_tasks
    with open(user_id + ".json", "w") as f:
        json.dump(my_json, f)
