#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

nexus2 =  {
    "host": "nxos2.lasthop.io", 
    "username":"pyclass", 
    "password": getpass(), 
    "device_type": "cisco_nxos",
}

net_connect = ConnectHandler(**nexus2)

print(net_connect.find_prompt())

output = net_connect.send_command("show lldp neighbors detail")

print(output)

net_connect.disconnect()
