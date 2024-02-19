#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    user_data = {
        "USER_ID": user_id,
        "tasks": []
    }

    for todo in todos:
        user_data["tasks"].append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"]
        })

    # Write data to JSON file
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    print("Data exported to", file_name)
