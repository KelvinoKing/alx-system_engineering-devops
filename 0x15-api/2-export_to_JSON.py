#!/usr/bin/python3
"""Import modules
"""
import csv
import json
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

        employee_name = users[employee_id - 1].get("username")

        # Export data to CSV
        export_to_csv(employee_id, employee_name, todos)

        # Export data to JSON
        export_to_json(employee_id, employee_name, todos)

    except requests.exception.RequestException as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)


def export_to_csv(employee_id, employee_name, todos):
    """Exports data to a csv file
    """
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"]
        writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
                quoting=csv.QUOTE_NONNUMERIC
                )

        for task in todos:
            task_status = task['completed']
            writer.writerow({
                "USER_ID": str(employee_id),
                "USERNAME": str(employee_name),
                "TASK_COMPLETED_STATUS": str(task_status),
                "TASK_TITLE": str(task['title'])
                })


def export_to_json(employee_id, employee_name, todos):
    """Export data to JSON
    """
    json_filename = f"{employee_id}.json"

    json_data = {
            str(employee_id): [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                    }
                for task in todos
                ]
            }

    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
