#!/usr/bin/python3
'''
    script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
import sys


def tasks_done(id):
    '''
        script that, using this REST API, for a given employee ID,
        returns information about his/her TODO list progress.
    '''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    number_tasks = len(todos_json)

    task_compleated = 0
    task_list = ""

    for task in todos_json:
        if task.get("completed") is True:
            task_compleated += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          task_compleated,
                                                          number_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    tasks_done(sys.argv[1])
