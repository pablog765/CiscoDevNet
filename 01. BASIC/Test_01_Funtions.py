# This is my first test with python, what is funtion print, format, etc
# Date: 23 y 24 november 2024 

# First Program
# print("¡Hola, Mundo!")

# Para enviar los comandos de cisco
commands = """enable
configure terminal 
interface {}
ip address {} {}
description Configure using Python
no shut 
exit"""
print(commands.format("loopback0", "192.168.0.1","255.255.255.0"))
