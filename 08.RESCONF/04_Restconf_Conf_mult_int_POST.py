################################################################################################
# Autor: Pablo Guachamin
# Fecha: 2025/01/08
# Utilice RESTCONF para configurar una interfaz en un dispositivo IOS-XE
# Este script utiliza el módulo requests para enviar una solicitud POST a un dispositivo IOS-XE
################################################################################################

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
import urllib3

# Desactivar advertencias de seguridad de urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


xe_url = 'https://182.66.121.82:8443/restconf/data/ietf-interfaces:interfaces'

xe_username = input('Enter username: ')
xe_password = getpass('Enter password: ')

xe_credentials = HTTPBasicAuth(username=xe_username, password=xe_password)

xe_headers = {"Content-type": "application/yang-data+json"}

user_input = int(input('Enter the number of interfaces to configure: '))    

for i in range(user_input):
    int_name = input('Enter the interface name (Sensitive case): ')
    int_ip = input('Enter the IP address: ')
    int_mask = input('Enter the subnet mask: ')
    int_payload = {
        "ietf-interfaces:interface": {
            "name": int_name,
            "description": "Added via RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": int_ip,
                        "netmask": int_mask
                    }
                ]
            }
        }
    }
int_configs = requests.post(url=xe_url, headers=xe_headers, auth=xe_credentials, json=int_payload, verify=False)
int_configs = requests.post(url=xe_url, headers=xe_headers, auth=xe_credentials, data=json.dumps(int_payload), verify=False)
print(f'Interface {int_name} configured successfully !!!!!! God Job !!!!!')