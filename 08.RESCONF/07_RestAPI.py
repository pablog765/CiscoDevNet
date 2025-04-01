import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input('Enter username: ')
password = getpass('Enter password: ')
asa_url = 'https://10.255.1.101/api/monitoring/device'
asa_creds = HTTPBasicAuth(username=username, password=password)
asa_headers = {"Content-type": "application/json"}
device_info = requests.get(url=asa_url, headers=asa_headers, auth=asa_creds, verify=False)
print(device_info.text)
print(device_info.status_code)