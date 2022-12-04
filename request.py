# Request Agent

# test request, remove when needed

import requests

response = requests.get("https://www.google.com")

print(response.status_code)
# print(response.text)