#!/usr/bin/python3
"""Import modules
"""
import csv
import json
import requests
import sys


def gather_data_from_api():
    """Fetches employees data from an API
    """
    api_url_users = "https://jsonplaceholder.typicode.com/users"
    api_url_todos = "https://jsonplaceholder.typicode.com/todos"

    try:
        response_users = requests.get(api_url_users)
        response_users.raise_for_status()
        users = response_users.json()

        response_todos = requests.get(api_url_todos)
        response_todos.raise_for_status()
        todos = response_todos.json()

        # Organize tasks by user ID
        user_tasks = {}
        for task in todos:
            user_id = task['userId']
            username = next(
                    user['username'] for user in users if user['id'] == user_id
                    )

            task_data = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.setdefault(str(user_id), []).append(task_data)

        # Export data to JSON
        export_to_json("todo_all_employees.json", user_tasks)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


def export_to_json(json_filename, user_tasks):
    """Export data to JSON
    """
    with open(json_filename, mode='w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    gather_data_from_api()
