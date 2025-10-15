import requests

url = "http://127.0.0.1:5000/generate"
data = {"goal": "Launch a new mobile app in 1 month"}

response = requests.post(url, json=data)

try:
    print(response.json())
except Exception as e:
    print("Error parsing JSON:", e)
    print("Raw response:", response.text)
