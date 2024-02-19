#!/usr/bin/python3
"""Exports to-do list information for all employees to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()  # Fetch all users
    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        # Store tasks for each user
        all_tasks[user_id] = [{
            "task": t["title"],
            "completed": t["completed"],
            "username": username
        } for t in todos]

    # Export all tasks to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
