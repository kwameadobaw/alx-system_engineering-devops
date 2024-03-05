#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    headers = {'User-Agent': 'Custom User Agent'}

    if after:
        params['after'] = after

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for child in children:
                if 'data' in child and 'title' in child['data']:
                    hot_list.append(child['data']['title'])

            if 'after' in data['data'] and data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
    return None
