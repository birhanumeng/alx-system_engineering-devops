#!/usr/bin/python3
""" export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()
    username = user.get("username")

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [argv[1], username, t.get("completed"), t.get("title")]
         ) for t in tasks]
