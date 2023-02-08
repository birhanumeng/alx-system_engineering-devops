#!/usr/bin/python3
"""export data in the JSON format of all employees"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("all_tasks.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for user in users}, jsonfile)
