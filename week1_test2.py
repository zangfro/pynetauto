from netmiko import ConnectHandler
from getpass import getpass

#net_connect = ConnectHandler(
#    host='cisco3.lasthop.io',
#    username='pyclass',
#    password=getpass(),
#    device_type='cisco_xe',
#    session_log='week1_log.txt'
#)

# convert above to a dict
device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_xe',
    "session_log": 'week1_log2.txt'
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command("show ip interface brief")

print(net_connect.find_prompt())
print(output)
