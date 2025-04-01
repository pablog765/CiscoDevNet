######################################################################
# Envia una configuración de Loopback 106 al dispositivo Cisco IOS-XE
# mediante NETCONF en formato XML.
# Se utiliza el módulo ncclient para la conexión NETCONF.
# Se utiliza edit_config() para enviar la configuración.
# Nota: El dispositivo debe tener habilitado el protocolo NETCONF.
######################################################################

from ncclient import manager
from getpass import getpass

# Credenciales
username = input("Enter your Username: ")
password = getpass("Enter your password: ")

# Detalles del router (Creamos un diccionario)
router_details = {
    'host': '182.66.121.82',
    'port': 8830,
    'username': username,
    'password': password,
    'hostkey_verify': False
}

# Payload XML en formato Nativo IOS-XE para configurar una Loopback
int_payload = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>160</name>
                <ip>
                    <address>
                        <primary>
                            <address>160.160.160.1</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
# Se utiliza un bloque de codigo try/except para manejar errores.

try:

    # Conexión NETCONF con "with   as" para cerrar la conexión automáticamente
    with manager.connect(**router_details) as netconf:
        print("Conexión exitosa con el dispositivo.")

        # Enviar configuración
        # edit_config() recibe dos argumentos: target y config, target para enviar la configuración a la running-config
        # y source para queremos obterner la configuración desde el dispositivo.
        # la variable int_payload contiene la configuración en formato XML.

        try:
            response = netconf.edit_config(target='running', config=int_payload)
            print("Respuesta del dispositivo:")
            print(response)
        except Exception as rpc_error:
            print("Error al enviar configuración:")
            print(rpc_error)

except Exception as conn_error:
    print(f"Error de conexión: {conn_error}")
