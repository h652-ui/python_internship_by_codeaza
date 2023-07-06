import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

response = requests.get('https://api.github.com')
print(response.content)
print(response.text)
print(response.headers)

response = requests.get('https://jsonplaceholder.typicode.com/users', params={'id': 1})
print(response.json())
from getpass import getpass
response = requests.get('https://meet.google.com/', auth=('hamidmuzaffar218@gmail.com', getpass()))
print(response.status_code)