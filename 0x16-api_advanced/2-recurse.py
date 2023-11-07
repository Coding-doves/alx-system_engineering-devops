#!/usr/bin/python3
'''function that queries Reddit API & print d titles of d first 10 hot posts'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    headers = {'User-Agent': 'MyApp/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        after = res.json().get('data').get('after')
        data = res.json().get('data').get('children')

        for val in data:
            hot_list.append(val.get('data').get('title'))
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list

    return None
