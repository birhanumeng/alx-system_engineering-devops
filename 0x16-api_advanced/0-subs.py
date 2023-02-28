#!/usr/bin/python3
"""Queries the number of subscribers in Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Finds the num of subscribers """

    req = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-Agent": "custom"})
    if (req.status_code == 200):
        return req.json().get("data").get("subscribers")
    else:
        return 0
