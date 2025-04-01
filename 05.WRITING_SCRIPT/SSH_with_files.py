############################################################################################################
# 1. Import the necessary libraries
# 2. Open the file containing the IP addresses of the routers
# 3. Open the file containing the commands to be executed on the routers
# 4. Open the file to write the output of the commands
# 5. Create a dictionary with the device details
# 6. Establish an SSH connection to the device
# For each command in the commands file, execute the command and write the output to the output file
# 7. Close the output file
# 8. Close the commands file
# 9. Close the IP addresses file
# 10. Print a message that the output is exported successfully to the file
# 11. Close the SSH connection
# Created by: Pablo G. 22/12/2024
############################################################################################################

from netmiko import ConnectHandler
from getpass import getpass

router_ip = open (r'/Users/pablo/Documents/Python_Projects/router_ip.txt', 'r')

# r - reading permissions
# w - writing permissions
# a - appending permissions
# r+ - reading and writing 

username = input('Enter your SSH username: ')
password = getpass('Enter your SSH password: ')

# Define the device type and the name of the file

for ip_add in router_ip:
    device_details = {
        'device_type': 'cisco_ios',
        'ip': ip_add,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**device_details)
    print('Connecting to the device...')
    print('SSH connection established to ' + ip_add)

    commands_details = open (r'/Users/pablo/Documents/Python_Projects/commands.txt', 'r')
    output_file = open (r'/Users/pablo/Documents/Python_Projects/configuration_output.txt', 'a')

    for commands in commands_details:
        details = net_connect.send_command(commands)
        output_file.write('The below information is fetched from ' + ip_add + '\n')
        output_file.write('The output of the command ' + commands + ' is: \n\n' + details + '\n\n')

    output_file.write('End of the output')
    output_file.write('-----------------------------------------------'+ '\n\n')
    output_file.close()
    commands_details.close()
    print('Output is exported successfully to the file')

router_ip.close()