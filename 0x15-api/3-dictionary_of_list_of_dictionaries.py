#!/usr/bin/python3
''' display on the standard output the employee Todo list progress '''

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = "{}/users".format(url)
    users = requests.get(user).json()
    worker_tasks = "{}/todos".format(url)
    tasks = requests.get(worker_tasks).json()
    emp_task = {use.get('id'): [{"username": username("username")
                                "task": tas.get("title"),
                                "completed": tas.get("completed"),
                                for tas in tasks if tas.get('userId')
                                == use.get('id')]
                                for use in username
                                }

    with open("todo_all_employees.json", 'w', encoding="utf-8") as file:
        json.dump(emp_task, file)
