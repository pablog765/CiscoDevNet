from telnetlib3 import telopt

username = 'admin'
password = 'cisco'
router_ip = '192.168.1.1'

tn = telopt(router_ip)
tn.write(username.encode('ascii') + b'\n')
tn.write(password + '\n')

commands = """
enable
conf t
interface loopback100
ip address 1.1.1.1 255.255.255.255
description LOOPBACK100 using telnet python
no shut
exit
"""
tn.write(commands.encode('ascii'))
print(tn.read_all().decode('ascii'))