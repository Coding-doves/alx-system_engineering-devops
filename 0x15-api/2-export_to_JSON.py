#!/usr/bin/python3
''' display on the standard output the employee Todo list progress '''

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = int(sys.argv[1])
    user = "{}/users/{}".format(url, id)
    username = requests.get(user).json().get('username')
    worker_tasks = "{}/todos".format(url)
    tasks = requests.get(worker_tasks).json()
    all_task = [tas for tas in tasks if tas.get('userId') == id]
    compd_task = {id: [{"task": tas.get("title"),
                        "completed": tas.get("completed"),
                        "username": username}
                       for tas in all_task if tas.get('userId')
                       == id]}

    with open("{}.json".format(id), 'w', encoding="utf-8") as file:
        json.dump(compd_task, file)
