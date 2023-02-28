#!/usr/bin/python3
"""Return the number of subscribers to a subreddit"""
import requests as r
from sys import argv


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    """
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/hot.json?limit=10"
    subs = r.get(endpoint.format(subreddit), headers=headers)
    if subs.status_code != 200:
        print(None)
        return 0
    subs = subs.json()
    if subs["kind"] == "Listing":
        for data in subs["data"]["children"]:
            print(data["data"]["title"])
    else:
        print(None)
