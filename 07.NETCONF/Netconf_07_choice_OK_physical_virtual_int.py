#############################################################################################################
# Con este script puedo configurar una interfaz fisica o virtual en un dispositivo Cisco IOS-XE a través de NETCONF
# Se observa un problema ya que la IP se asigna a la interfaz GigabitEthernet3 pero como secondary
# Para evitar que se asigne como secondary se debe configurar en el template de la interfaz la siguiente linea:
# <interface operation = "replace">
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

# Establish NETCONF connection
netconf = manager.connect(**device_details)
print("Connection to the device established successfully.......")

# Number of interfaces to configure
no_of_int = int(input("Enter the number of interfaces to configure: "))

for int_conf in range(0, no_of_int):
    # Conditional statement to chose the kind of interface do you want to configure
    int_type = int(input("Enter the interface type: \n1. GigabitEthernet\n2. Loopback\n \n Please make a choice: \n"))  

    if int_type == 1:
        type_int = "ethernetCsmacd"
    elif int_type == 2:
        type_int = "softwareLoopback"

    # Declare variable to interfaces configuration
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the IP address: ")
    int_mask = input("Enter the subnet mask: ")
    int_desc = input("Enter the description: ")

    # Interface configuration template
    interface_payload = f"""
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation = "replace">   # Para evitar que se asigne como secondary
                <name>{int_name}</name>
                <description>{int_desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{type_int}</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{int_ip}</ip>
                        <netmask>{int_mask}</netmask>
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