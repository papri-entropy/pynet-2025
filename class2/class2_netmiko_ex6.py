#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

import time

password = getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "netmiko_ex6_cisco4.txt"
}



net_connect = ConnectHandler(**cisco4)

print(net_connect.find_prompt())

print(net_connect.config_mode())

print(net_connect.exit_config_mode())

net_connect.write_channel("disable\n")

time.sleep(2)

print(net_connect.read_channel())

print(net_connect.find_prompt())

net_connect.enable()

print(net_connect.find_prompt())





net_connect.disconnect()
