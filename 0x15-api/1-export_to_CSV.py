#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed_tasks = []
    for todo in todos:
        completed_tasks.append([
            user_id,
            user["username"],
            "completed" if todo["completed"] else "not completed",
            todo["title"]
        ])

    # Write data to CSV file
    file_name = "{}.csv".format(user_id)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(completed_tasks)

    print("Data exported to", file_name)
