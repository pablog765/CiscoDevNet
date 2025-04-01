################################################################################################
# 1. Establish a connection to the CSR1000v NETCONF agent.
# 2. Display the running configuration.
# 3. Close the NETCONF session.
#
# Note: The device is running a NETCONF agent and the agent is enabled for NETCONF over SSH.
# The device is also configured with the correct NETCONF port, in this case is 8830 but the default port is 830.
# The device is also configured with RESCONF over SSH port: 8443 but by default is 4330.
# The device is also configured with the SSH port: 8022 but by default is 22.
################################################################################################

from ncclient import manager
# import xml.dom.minidom 
from xml.dom.minidom import parseString
from getpass import getpass

username = input("Enter your Username:    ")           # Student
password = getpass("Enter your password:  ")           # PyNet@123

router_details = {
    'host': '182.66.121.82',
    'port': 8830,
    'username': username,
    'password': password,  
    'hostkey_verify': False
}

netconf=manager.connect(**router_details)
print("Netconf session connected with the device successfully.......!   ")

running_config = netconf.get_config(source='running').data_xml
print("The running configuration of the device is: " + router_details['host'] + "\n")
print("=====================================================")
print(running_config)
print("=====================================================")
pretty_running = parseString(running_config).toprettyxml()
print(pretty_running)
#print(xml.dom.minidom.parseString(running_config).toprettyxml())

myfile = open("running_config.xml", "w")
myfile.write(pretty_running)
myfile.close()

netconf.close_session()
print("Netconf session closed successfully.......!   ")
