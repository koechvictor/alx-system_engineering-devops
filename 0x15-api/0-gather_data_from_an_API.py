#!/usr/bin/python3
"""Get the todo list for one user and print info"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    resp = requests.get(url)
    tasks = resp.json()
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    resp = requests.get(url)
    user = resp.json()

    total = 0
    done = 0
    for task in tasks:
        if task.get("completed"):
            done = done + 1
        total = total + 1

    tasks = [t for t in tasks if t.get("completed")]
    name = user.get("name")
    if name is None:
        exit()
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in tasks:
        print("\t " + task.get("title"))
