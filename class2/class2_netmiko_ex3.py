#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "netmiko_ex1a_cisco4.txt"
}



net_connect = ConnectHandler(**cisco4)

print(net_connect.find_prompt())

show_ver = net_connect.send_command("show version", use_textfsm=True)

print("*" * 40)
print(show_ver) 
print("*" * 40)

show_lldp = net_connect.send_command("show lldp neighbors", use_textfsm=True)

print(show_lldp)
print("*" * 40)
print(type(show_lldp))
print("*" * 40)
print(show_lldp[0]["neighbor_interface"])
print("*" * 40)


net_connect.disconnect()
