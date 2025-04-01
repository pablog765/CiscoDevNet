#############################################################################################################
# Con este script puedo configurar una interfaz en un dispositivo Cisco IOS-XE a través de NETCONF
# Se observa un problema ya que la IP se asigna a la interfaz GigabitEthernet3 pero como secondary
#############################################################################################################


from ncclient import manager
from getpass import getpass

username = input("Enter your Username: ")  # Student
password = getpass("Enter your password: ")  # PyNet@123

# Device details
device_details = {
    "host": "182.66.121.82",
    "port": 8830,
    "username": username,
    "password": password,
    "hostkey_verify": False
}

netconf = manager.connect(**device_details)
print("Connection to the device established successfully.......")

# Interface configuration template
interface_payload = """

<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>GigabitEthernet3</name>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>192.171.3.19</ip>
					<netmask>255.255.255.0</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
    </interfaces>
</config>
"""

int_config = netconf.edit_config(interface_payload, target="running")
print("Interface configuration sent successfully.......")
print(int_config)