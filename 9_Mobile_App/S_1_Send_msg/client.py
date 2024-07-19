import requests

url = 'https://b0eb-2402-4000-20c3-d124-3e-9fe6-45eb-bec5.ngrok-free.app'
data = {
    "message": "Hello from client",
    "timestamp": "2024-07-18T12:00:00"
}

response = requests.post(url, json=data)

print(f"Server response: {response.json()}")
