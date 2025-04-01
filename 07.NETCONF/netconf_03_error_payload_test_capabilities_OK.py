from ncclient import manager
from getpass import getpass

# Credenciales
username = input("Enter your Username: ")  # Student
password = getpass("Enter your password: ")  # PyNet@123

router_details = {
    'host': '182.66.121.82',
    'port': 8830,
    'username': username,
    'password': password,
    'hostkey_verify': False
}

try:
    with manager.connect(**router_details) as netconf:
        print("Conexión exitosa con el dispositivo.")

        # Verificar capacidades
        print("Capacidades del dispositivo:")
        for cap in netconf.server_capabilities:
            print(cap)

        # XML simplificado
        int_payload = """
        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>Loopback160</name>
                    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                    <enabled>true</enabled>
                </interface>
            </interfaces>
        </config>
        """
        
        # Enviar configuración
        response = netconf.edit_config(target='running', config=int_payload)
        print("Respuesta del dispositivo:")
        print(response)

except Exception as e:
    print(f"Error: {e}")