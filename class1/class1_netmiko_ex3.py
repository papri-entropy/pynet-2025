#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "netmiko_ex3_cisco3.txt"
}



net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())

print(net_connect.send_command("show version"))



net_connect.disconnect()
