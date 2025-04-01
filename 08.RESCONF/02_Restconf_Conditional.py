import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import urllib3

# Desactivar advertencias de seguridad de urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

xe_url = 'https://182.66.121.82:8443/restconf/data/ietf-interfaces:interfaces'

xe_username = input('Enter username: ')
xe_password = getpass('Enter password: ')

xe_credentials = HTTPBasicAuth(username=xe_username, password=xe_password)

xe_headers = {"Accept": "application/yang-data+json"}


response = requests.get(url=xe_url, headers=xe_headers, auth=xe_credentials, verify=False)

if response.status_code == 200:
    print("Request was successful")
    print(response.text)
elif response.status_code == 404:
    print("Resource not found. Please check the URL.")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)