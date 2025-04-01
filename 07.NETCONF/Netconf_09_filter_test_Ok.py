from ncclient import manager
from ncclient.xml_ import to_ele
from getpass import getpass

# Device details
device_details = {
    "host": "182.66.121.82",
    "port": 8830,
    "username": 'Student',
    "password": 'PyNet@123',
    "hostkey_verify": False
}

# Establish NETCONF connection
with manager.connect(**device_details) as netconf:
    print("Connected to the device successfully.")

    # Filter for interfaces
    int_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    try:
        # Convert XML string to XML element
        int_filter_xml = to_ele(int_filter)
        print("Filter parsed successfully.")

        # Get running configuration
        running_config = netconf.get_config(filter=int_filter_xml, source="running")
        print("Running Configuration:")
        print(running_config.xml)
    except Exception as e:
        print(f"Error: {e}")
