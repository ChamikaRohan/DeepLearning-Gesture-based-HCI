import requests

# Replace 'server_ip' with the actual IP address of the server
server_ip = '192.168.1.10'  # Example IP address
server_port = 5000

# Test the GET request
response = requests.get(f'http://192.168.8.131:5000/hello')
if response.status_code == 200:
    print(response.json())

# Test the POST request
payload = {'message': 'Hello, Flask!'}
response = requests.post(f'http://192.168.8.131:5000/echo', json=payload)
if response.status_code == 200:
    print(response.json())
