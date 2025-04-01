

from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString
from xmltodict import parse  # Importo la función parse para convertir el objeto XML en un diccionario

#username = input("Enter your Username: ")  # Student
#password = getpass("Enter your password: ")  # PyNet@123

# Device details
device_details = {
    "host": "182.66.121.82",
    "port": 8830,
    "username": 'Student',
    "password": 'PyNet@123',
    "hostkey_verify": False
}


# Establish NETCONF connection
netconf = manager.connect(**device_details)
print("Connection to the device established successfully.......")

# filter
int_filter = """
<filter xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
"""

running_config = netconf.get_config(source = "running", filter = int_filter)
pretty_config = parseString(running_config.xml).toprettyxml()
print("Running configuration successfully.......")

# Convert the XML object to a dictionary
dict_data = parse(pretty_config)
#print(dict_data['rpc-reply']['data']["interfaces"]['interface'][0]['name'])


list_of_intf = dict_data['rpc-reply']['data']["interfaces"]['interface']
for intf in list_of_intf:
    print ("-------------------------------------------------------")
    #print(intf['name'])
    print(intf['ipv4']['address']['ip'])
    #print(f"Interface Name: {intf['name']['#text']}")
    #print(f"Interface Description: {intf['description']}")
    #print(f"Interface Type: {intf['type']['#text']}")
    #print(f"Interface Enabled: {intf['enabled']}")
    #print("-------------------------------------------------------")

