

from netmiko import ConnectHandler
from getpass import getpass

routers = {
    "R1":"192.168.30.133",
    "R2":"192.168.30.134",
    "R3":"192.168.30.135"
}


print(routers)
user_choice = input("Enter the device that you wish to configure (R1/R2/R3): ")
user_choice = user_choice.upper()
router_ip = routers[user_choice]

username = input("Enter your username: ")
password = getpass("Enter your password: ")

device_details = {
    'ip':router_ip,
    'username':username,
    'password':password,
    'device_type':'cisco_ios'
}

ssh = ConnectHandler(**device_details)
print("SSH Connection was established successfully with " + router_ip)

no_of_int = int(input("Enter the number of interfaces that you wish to configure: "))

for int_configs in range(0, no_of_int):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

    commands = [f'interface {int_name}', f'ip address {int_ip} {int_mask}', 'no shutdown', f'desc {int_desc}']
    int_configurations = ssh.send_config_set(commands)
    print(int_configurations)

    int_details = ssh.send_command(input("Enter the show commands that you wish to run for verification: "))
    print(int_details)

ssh.save_config()
print("Configurations were saved successfully..!")

ssh.disconnect()