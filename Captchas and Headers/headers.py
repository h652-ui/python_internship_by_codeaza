import requests

# Send a GET request to the URL
url = "https://www.openai.com"
response = requests.get(url)

# Print the request headers
print("\nRequest Headers:\n")
for header, value in response.request.headers.items():
    print(f"{header}: {value}")

# Print the response headers
print("\nResponse Headers:\n")
for header, value in response.headers.items():
    print(f"{header}: {value}")
