########################################################################################
#  Script para configurar múltiples interfaces en un router
#  y guardar la configuración en un archivo de texto al cual se le
#  añade la fecha y hora de la configuración y pide al usuario colocar un 
#  comando para mostrar el estado de las interfaces y nombre del archivo
#  2024-12-21 Pablo G.
########################################################################################

from netmiko import ConnectHandler
from getpass import getpass
import datetime

username = input("Enter your username: ")
password = getpass("Enter your password: ")
router_ip = input("Enter the IP address of the router: ")

device_details = {
    'ip':router_ip,
    'username':username,
    'password':password,
    'device_type':'cisco_ios'
}

SSH_Connect = ConnectHandler(**device_details)
print("Conectado al router..." + router_ip )
num_interfaces = int(input("Enter the number of interfaces that you wish to configure: "))

for i in range(num_interfaces):
    int_name = input("Enter the name of the interface: ")
    int_ip = input("Enter the IP address of the interface: ")
    int_mask = input("Enter the subnet mask of the interface: ")
    int_desc = input("Enter the description of the interface: ")

    commands = [
        'interface ' + int_name,
        'ip address ' + int_ip + ' ' + int_mask,
        'description ' + int_desc,
        'no shutdown'
    ]

    print(f"\nAplicando configuración para {int_name}...")
    SSH_Connect.send_config_set(commands)
    print(f"¡Configuración de {int_name} completada!")

# Mostrar el estado de las interfaces a traves de un comando:
int_details = SSH_Connect.send_command(input('Enter the show command that you wish to run for verification'))
print(int_details)

# Vamos a enviar la configuración de todas las interfaces a un archivo de texto
with open(r'/Users/pablo/Documents/Python_Projects/{}.txt'.format(input('Enter the filename that you wish to save: ')), 'w') as myfile:
    myfile.write("Configuración de las interfaces del router\n")
    myfile.write(int_details)
    myfile.write("\nThis configuration is saved at " + str(datetime.datetime.now()) + "\n")

SSH_Connect.save_config()
print("\nGuardando la configuración...")

print("\n¡Configuración de todas las interfaces completada!")
SSH_Connect.disconnect()
