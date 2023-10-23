#!/usr/bin/python3
''' display on the standard output the employee Todo list progress '''

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = int(sys.argv[1])
    user = "{}/users/{}".format(url, id)
    name = requests.get(user).json().get('name')
    worker_tasks = "{}/todos".format(url)
    tasks = requests.get(worker_tasks).json()
    all_task = [tas for tas in tasks if tas.get('userId') == id]
    compd_task = [tas for tas in all_task if tas.get('completed')]

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(compd_task), len(all_task)))

    for task in compd_task:
        print('\t {}'.format(task.get('title')))
