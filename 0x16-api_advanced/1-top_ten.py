#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    # Check if subreddit is provided
    if subreddit is None or not isinstance(subreddit, str):
        print("Subreddit name should be provided as a string.")
        return

    # Reddit API request headers
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Reddit API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        # Sending GET request to Reddit API
        response = requests.get(url, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Extracting JSON data
        data = response.json()

        # Check if subreddit exists
        if 'error' in data:
            print(f"Subreddit '{subreddit}' not found.")
            return

        # Extracting posts
        posts = data['data']['children']

        # Printing titles of the first 10 posts
        for post in posts[:10]:
            print(post['data']['title'])

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


# Example usage
top_ten('python')