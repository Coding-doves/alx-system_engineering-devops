#!/usr/bin/python3
''' function that queries Reddit API and returns the number of subscribers '''
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        val = data.get('data').get('subscribers')
        return val

    return 0
