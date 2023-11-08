#!/usr/bin/python3
import requests
import datadog_api_client
# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "f0bdffa6eee17992205164f460c0a545"
api_app_key = "3ae7c57e27110bbc542734f175d98312267a6efc1"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:263052-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
