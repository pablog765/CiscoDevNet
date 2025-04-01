################################################################################################
# In this part we try to configure the interface on the router using NETCONF.
# The interface should be a loopback interface with an IP address and a netmask.
# Basado en un ejemplo de configuración encontrado en [URL] bajo licencia MIT.
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
try:
    with manager.connect(**router_details) as netconf:
        print("Netconf session connected with the device successfully.......!   ")
except Exception as e:
        print("An error occurred: " + str(e))

int_payload = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
			<name>Loopback160</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>160.160.160.1</ip>
					<netmask>255.255.255.255</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
	    </interface>
    </native>
</config>
"""

int_config = netconf.edit_config(int_payload, target='condidate')
print("The interface configuration has been added to the device: " + router_details['host'] + "\n")
print("=====================================================")
print(int_config)
