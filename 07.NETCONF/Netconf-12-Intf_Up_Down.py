from netmiko import ConnectHandler
import xmltodict
from ncclient import manager

device_details = {
    "host": "182.66.121.82",
    "port": 8830,
    "username": 'Student',
    "password": 'PyNet@123',
    "hostkey_verify": False
}

def get_interfaces_status(device_details):
    # Establish NETCONF connection
    netconf = manager.connect(**device_details)
    print("Connection to the device established successfully.......")
    print(netconf.connected)

    netconf_filter = """
    <filter xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    netconf_reply = netconf.get(filter=netconf_filter)
    interfaces = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]

    up_count = 0
    down_count = 0

    for interface in interfaces:
        if interface["oper-status"] == "up":
            up_count += 1
        else:
            down_count += 1

    # Mostrar el estado de las interfaces a través de un comando:
    int_details = netconf.get(input('Enter the show command that you wish to run for verification: '))
    print(int_details)

    return up_count, down_count

if __name__ == "__main__":
    up_count, down_count = get_interfaces_status(device_details)
    print(f"Interfaces UP: {up_count}")
    print(f"Interfaces DOWN: {down_count}")