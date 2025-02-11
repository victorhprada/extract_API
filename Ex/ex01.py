import requests

url = "https://api.github.com/events"

response = requests.get(url)

print(response.json())

url2 = 'https://www.google.com'

response2 = requests.get(url2)

print(response2)
