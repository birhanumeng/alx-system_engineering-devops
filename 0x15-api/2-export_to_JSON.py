#!/usr/bin/python3
""" export data in the json format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()
    username = user.get("username")

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in tasks]}, jsonfile)
