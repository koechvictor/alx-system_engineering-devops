#!/usr/bin/python3
"""Return the number of subscribers to a subreddit"""
import requests as r
from sys import argv


def recurse(subreddit, hot_list=[], p={"limit": 1}):
    url = "https://reddit.com/r/" + subreddit + "/hot.json"
    ua = {'User-agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=ua, params=p)
    data = resp.json().get("data", {})
    aft = data.get("after", None)
    l = data.get("children", [])
    if aft is None or len(l) == 0:
        if len(hot_list) == 0:
            return None
        return hot_list
    hot_list.append(l[0].get("data", {}).get("title", ""))
    p["after"] = aft
    return recurse(subreddit, hot_list, p)
