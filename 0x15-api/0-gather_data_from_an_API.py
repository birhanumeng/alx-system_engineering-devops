#!/usr/bin/python3
"""returns information about employee's TODO list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(tasks)))

    [print("\t {}".format(job)) for job in completed]
