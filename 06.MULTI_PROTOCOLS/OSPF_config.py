# You can choose to run this script by running the command: python OSPF_config.py
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
print("\nSSH Connection was established successfully with " + router_ip)

# Ask the user about which routing protocol they are willing to configure on the router. (Static Routing, EIGRP or OSPF)

print('\nWelcome to the Routing Protocol Configuration Script')

user_input = int(input('''Enter the routing protocol that you wish to configure ? 
                       1. Static Routing
                       2. EIGRP
                       3. OSPF
                       Please make a choice (1 / 2 / 3): '''))

if user_input == 1:
    print('\nYou have chosen to configure Static Routing on the router. \nPlease provide the details below: ')
    user_input1 = int(input('''\nEnter the number of static routes that you wish to configure: '''))
    
    for static_routes in range(0, user_input1):
        static_network = input('Enter the network that you wish to advertise: ')
        static_mask = input('Enter the subnet mask: ')
        next_hop = input('Enter the next hop IP address: ')

        static_config = [f'ip route {static_network} {static_mask} {next_hop}']
        static_configurations = ssh.send_config_set(static_config)
        print(static_configurations)

        static_details = ssh.send_command('show run | inc ip route')
        print(static_details)
    
elif user_input == 2:
        print('You have chosen to configure EIGRP on the router. \nPlease provide the details below: ')
        user_input2 = int(input('''Enter the number of routes that you wish to configure: '''))
        eigrp_as = input('Enter the EIGRP AS number: ')

        for eigrp_configs in range(0, user_input2):
            
            eigrp_network = input('Enter the network that you wish to advertise: ')
            eigrp_wildcard = input('Enter the wildcard mask: ')

            eigrp_config = [f'router eigrp {eigrp_as}', f'network {eigrp_network} {eigrp_wildcard}']
            eigrp_configurations = ssh.send_config_set(eigrp_config)
            print(eigrp_configurations)

            eigrp_details = ssh.send_command('show run | sec router eigrp')
            print(eigrp_details)

            eigrp_route = ssh.send_command('show ip route eigrp')
            print(eigrp_route)

elif user_input == 3:
        print('You have chosen to configure OSPF on the router. \nPlease provide the details below: ')

        ospf_process = input("Enter the OSPF process ID: ")
        no_of_routes = int(input("Enter the number of routes that you wish to advertise using OSPF: "))
    
        for ospf in range(0, no_of_routes):
            ospf_network = input("Enter the network that you wish to advertise: ")
            wilcard_mask = input("Enter the wildcard mask: ")
            ospf_area = input("Enter the OSPF area: ")

            ospf_config = [f'router ospf {ospf_process}', f'network {ospf_network} {wilcard_mask} area {ospf_area}']
            ospf_configurations = ssh.send_config_set(ospf_config)
            print(ospf_configurations)

            ospf_details = ssh.send_command('show run | sec router ospf')
            print(ospf_details)

            ospf_route = ssh.send_command('show ip route ospf')
            print(ospf_route)

else:
    print('Invalid choice. Please try again..!')


ssh.save_config()
print("Configurations were saved successfully..!")

ssh.disconnect()