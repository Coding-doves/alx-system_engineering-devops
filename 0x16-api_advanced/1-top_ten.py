#!/usr/bin/python3
'''function that queries Reddit API & print d titles of d first 10 hot posts'''
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get('data').get('children')

        for val in data:
            print(val.get('data').get('title'))
    else:
        print(None)
