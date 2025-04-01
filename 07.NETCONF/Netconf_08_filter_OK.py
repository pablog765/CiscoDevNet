#############################################################################################################
# Este Scrip obtine la configuración de todos los interfaces de un dispositivo utilizando un filtro
# El filtro se define en la variable int_filter
# Se obtiene la configuración en formato XML y se imprime en pantalla
# Se guarda la configuración en un archivo XML
# Se utiliza el método get_config() para obtener la configuración de un dispositivo
# Se utiliza el método parseString() para convertir la configuración en formato XML a un formato más legible
# Se utiliza el método toprettyxml() para imprimir la configuración en un formato más legible
# Se utiliza el método open() para guardar la configuración en un archivo XML
# Se utiliza el método write() para escribir la configuración en el archivo XML
# Se utiliza el método close() para cerrar el archivo XML
#############################################################################################################


from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString
from xmltodict import parse  # Importo la función parse para convertir el objeto XML en un diccionario

#username = input("Enter your Username: ")  # Student
#password = getpass("Enter your password: ")  # PyNet@123

# Device details
device_details = {
    "host": "182.66.121.82",
    "port": 8830,
    "username": 'Student',
    "password": 'PyNet@123',
    "hostkey_verify": False
}


# Establish NETCONF connection
netconf = manager.connect(**device_details)
print("Connection to the device established successfully.......")

# filter
int_filter = """
<filter xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
"""

running_config = netconf.get_config(source = "running", filter = int_filter)
pretty_config = parseString(running_config.xml).toprettyxml()
print("Running configuration successfully.......")
print(pretty_config)

myfile = open(r"running_config_filter.xml", "w")
myfile.write(pretty_config)
myfile.close()

