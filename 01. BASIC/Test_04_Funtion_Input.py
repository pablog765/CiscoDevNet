# uso de la funcion INPUT

interface_name = input('Enter the interface name: ')
interface_ip = input('Enter the interface IP address: ')
interface_mask = input("Enter the interface subnet mask: ")
interface_desc = input("Enter the interface description: ")


commands = """"
enable
conf t
interface {int_name}
ip address {ip} {mask}
description {description_this}
no shut
exit
"""
# print(commands.format(ip = '200.10.1.1', mask = '255.255.255.252', int_name = 'gigaethernet0/0', description_this = ' esta es la description '))

print(commands.format(ip = interface_ip, mask = interface_mask, int_name = interface_name, description_this = interface_desc))