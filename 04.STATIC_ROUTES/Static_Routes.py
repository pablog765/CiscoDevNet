# Para crear rutas staticas en 3 routers
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

sshConnect= ConnectHandler(**device_details)
print("SSH Connection was established successfully with: " + router_ip)

no_of_routes = int(input("Enter the number of routes that you wish to configure: "))

for route_configs in range(0, no_of_routes):
    
    route_ip = input("Enter the route IP address: ")
    route_mask = input("Enter the route subnet mask: ")
    next_hop = input("Enter the next_hop: ")

    commands = [f'ip route {route_ip} {route_mask} {next_hop}']
    Configuration= sshConnect.send_config_set(commands)
    print(Configuration)

    static_details = sshConnect.send_command('show run | inc ip route')
    print(static_details)

    route_details = sshConnect.send_command(input("Enter the show commands that you wish to run for verification: "))
    print(route_details)
    print('We are continue..........Enter the next value............')

sshConnect.save_config()
print("Configurations were saved successfully..!")

sshConnect.disconnect()