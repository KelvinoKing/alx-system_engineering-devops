#!/usr/bin/python3
"""Import modules
"""
import requests
import sys


def gather_data_from_api(employee_id):
    """Fetches employees data from an API
    """
    api_url_user = "https://jsonplaceholder.typicode.com/users"
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        response_user = requests.get(api_url_user)
        response_user.raise_for_status()
        users = response_user.json()

        response_todos = requests.get(api_url)
        response_todos.raise_for_status()
        todos = response_todos.json()

        employee_name = users[employee_id - 1].get("name")

        completed_tasks = [todo for todo in todos if todo['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_number_of_tasks))

        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exception.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
