# Import the library into your code.
from netmiko import ConnectHandler

# Create a dictionary for your device defining required parameters, here the device is Cisco virtual IOS.
R1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.30.133',
    'username': 'admin',
    'password': 'cisco',

}

# Call the ConnectHandler module to connect with the router. (** before the dictionary name is used to tell the
# python to consider the content of the dictionary as key-value pairs instead of single elements.)

ssh = ConnectHandler(**R1)
print('Connection to R1 established successfully')
print(ssh.find_prompt())

# Ask the user about all of the required information and collect the data into the variables like shown below.
int_name = input('Enter the interface name: ')
int_ip = input('Enter the interface IP address: ')
int_mask = input('Enter the interface subnet mask: ')
int_desc = input('Enter the interface description: ')


# Create the list of commands and concatenate the variables into the commands to make it work as per the user
# provided information. Send the list of commands to the router using send_config_set().

commands = [
    'interface ' + int_name,
    'ip address ' + int_ip + ' ' + int_mask,
    'description ' + int_desc
]
int_conf = ssh.send_config_set(commands)
print(int_conf)

# Send “show ip interface brief” to the router for verification. For sending commands into the Privileged mode we
# use send_command().

int_details = ssh.send_command('show ip interface brief')
print(int_details)

# Save the changes permanently on router using save_config().

ssh.save_config()

# Close the connection using disconnect().

ssh.disconnect()
print('Connection to R1 closed successfully')
