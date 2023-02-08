#!/usr/bin/python3
"""returns information about employee's TODO list progress"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()
    userId = argv[1]
    username = user.get("username")

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
