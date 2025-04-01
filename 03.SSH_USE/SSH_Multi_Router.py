
########################################################
# Las ventajas de este script son:
# Configura múltiples routers en una sola ejecución
# Permite configurar múltiples interfaces por router
# Maneja las credenciales de forma segura
# Verifica y guarda automáticamente la configuración
# Es interactivo y flexible
# 2024-12-15 Pablo G.
########################################################

# Import the library into your code. Getpass is used to collect the information in hidden manner.

from netmiko import ConnectHandler
from getpass import getpass

# Collect the information about the username and password.

username = input('Enter your username: ')
password = getpass('Enter your password: ')

# Create a list of Routers which contains the IP address of all the routers.

R1 = '192.168.30.133'
R2 = '192.168.30.134'
R3 = '192.168.30.135'

devices = [R1, R2, R3]

# Create a for loop which can loop through the data of list devices and can connect to the routers of list one by
# one like shown below. All of the remaining commands will be a part of this for loop.  

for router in devices:
    device = {
        'device_type': 'cisco_ios',
        'ip': router,
        'username': username,
        'password': password
    }

    ssh = ConnectHandler(**device)
    print('The connection was established successfully with ' + router)

    user_input = int(input('Enter the number of the interface to be configured: '))
    for interface in range(0, user_input):
        int_name = input('Enter the name of the interface: ')
        int_ip = input('Enter the IP address of the interface: ')
        int_mask = input('Enter the subnet mask of the interface: ')
        int_desc = input('Enter the description of the interface: ')

        # Send the commands to the router to configure the interface.
        commands = [
            'interface ' + int_name,
            'ip address ' + int_ip + ' ' + int_mask,
            'description ' + int_desc,
            'no shutdown'
        ]
        int_conf = ssh.send_config_set(commands)
        print(int_conf)

    # Send “show ip interface brief” to the router for verification. For sending commands into the Privileged mode we
    # use send_command().

    int_details = ssh.send_command('show ip interface brief')
    print(int_details)

    # Save the changes permanently on router using save_config().

    ssh.save_config()
    ssh.disconnect()    

