# API

***0-gather_data_from_an_API.py*** -> *script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.*

***1-export_to_CSV.py*** -> *Using what you did in the task #0, extend your Python script to export data in the CSV format.*

***2-export_to_JSON.py*** -> *Using what you did in the task #0, extend your Python script to export data in the JSON format.*

***3-dictionary_of_list_of_dictionaries.py*** -> *Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json*
