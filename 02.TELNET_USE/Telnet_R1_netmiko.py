from netmiko import ConnectHandler

# Configuración del dispositivo creando el diccionario device
device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.30.133',
    'username': 'admin',
    'password': 'cisco',
}

# Conectar al router con el metodo ConnectHandler
net_connect = ConnectHandler(**device)

# Comandos a ejecutar; es una lista de comandos 
commands = [
    #'enable',
    #'configure terminal',
    'interface loopback104',
    'ip address 4.4.4.4 255.255.255.255',
    'description LOOPBACK104 using telnet python',
    'no shut',
    'exit',
    'end',
    'show interfaces description',
]

# Ejecutar comandos
output = net_connect.send_config_set(commands)

# Mostrar el output o resultado de los comandos ejecutados
print(output)
print('Configuration complete')
# Cerrar conexión
net_connect.disconnect()