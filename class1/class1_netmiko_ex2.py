#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "netmiko_ex2_nxos1.txt"
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "netmiko_ex2_nxos2.txt"
}

devices = [nxos1, nxos2]

for device in devices:
    net_connect = ConnectHandler(**device)

    print(net_connect.find_prompt())

    net_connect.disconnect()
