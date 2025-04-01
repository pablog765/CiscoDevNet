import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
from json import dumps
from urllib3 import disable_warnings

xe_username = input('Enter username: ')
xe_password = getpass('Enter password: ')

xe_credentials = HTTPBasicAuth(username=xe_username, password=xe_password)
xe_headers = {"Content-type": "application/yang-data+json"}

user_input = int(input('Enter the number of interfaces to configure: '))

for abc in range(user_input):
    int_type = input('Enter the interface type wich you would like to configure: \n1. Physical Interface\n2. Loopback Interface\n Please make a choice !!!: ')
    if int_type == '1':
        int_name = input('Enter the interface name (Sensitive case): ')
        xe_url = f'https://182.66.121.82:8443/restconf/data/ietf-interfaces:interfaces/interfce={int_name}'
        #int_type_value = 'iana-if-type:ethernetCsmacd'
        int_type_value = 'ethernetCsmacd'

    elif int_type == '2':
        int_name = 'Loopback' + input('Enter the interface number: ')
        xe_url = 'https://182.66.121.82:8443/restconf/data/ietf-interfaces:interfaces'
        int_type_value = 'softwareLoopback'

    int_ip = input('Enter the IP address: ')
    int_mask = input('Enter the subnet mask: ')

    int_payload = { 
        "ietf-interfaces:interface": {
            "name": int_name,
            "description": "Added via RESTCONF",
            "type": "iana-if-type:{}".format(int_type_value),
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
int_configs = requests.post(url=xe_url, headers=xe_headers, auth=xe_credentials, data=dumps(int_payload), verify=False)
print(f'Interface {int_name} configured successfully !!!!!! God Job !!!!!')
# End of the script
