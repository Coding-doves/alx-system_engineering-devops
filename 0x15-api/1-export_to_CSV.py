#!/usr/bin/python3
''' display on the standard output the employee Todo list progress '''

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = int(sys.argv[1])
    user = "{}/users/{}".format(url, id)
    u_name = requests.get(user).json().get('username')
    worker_tasks = "{}/todos".format(url)
    tasks = requests.get(worker_tasks).json()
    emp_task = [[id, u_name, task.get("completed"), task.get("title")]
                for task in tasks if id == task.get('userId')
                ]

    with open("{}.csv".format(id), 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for row in emp_task:
            writer.writerow(row)
