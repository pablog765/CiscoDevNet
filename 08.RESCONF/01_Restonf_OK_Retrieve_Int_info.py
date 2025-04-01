
############################################################################################################
# Author: Pablo Guachamin 
# Date: 2024-01-08
# Description: you will have learned how to use the requests library to send a RESTCONF GET request to a
# network device, retrieve interface information using JSON format, and display the response.
############################################################################################################

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass 

# We define the URL to the RESTCONF API for retrieving interface informations of the Cisco XE device
xe_url = 'https://182.66.121.82:8443/restconf/data/ietf-interfaces:interfaces'

# We define the username and password to authenticate to the Cisco XE device
xe_username = input('Enter username: ')
xe_password = getpass('Enter password: ')

xe_credentials = HTTPBasicAuth(username=xe_username, password=xe_password)

# We define the variables headers for the RESTCONF API request include the accpeted content type
xe_headers = {"Accept": "application/yang-data+json"}

# We send the RESTCONF GET request to the Cisco XE device to retrieve the interface details
int_details = requests.get(url=xe_url, headers=xe_headers, auth=xe_credentials, verify=False)

# The statement below prints the response content and the HTTP status code to the terminal.
print(int_details.status_code)
print(int_details.text)
