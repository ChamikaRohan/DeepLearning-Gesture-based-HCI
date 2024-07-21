import requests

# Replace 'server_ip' with the actual IP address of the server
server_ip = '192.168.8.131'  # Example IP address
server_port = 80

response = requests.get(f'http://{server_ip}:{server_port}/hello')
if response.status_code == 200:
    print(response.json())

file_path = 'img.jpg'
with open(file_path, 'rb') as file:
    files = {'file': (file_path, file, 'multipart/form-data')}
    response = requests.post(f'http://{server_ip}:{server_port}/file', files=files)
if response.status_code == 200:
    print(response.json())

