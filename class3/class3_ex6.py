#!/usr/bin/env python

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from getpass import getpass
import yaml
from pprint import pprint


password = getpass()

filename = ".netmiko.yml"

with open(filename) as f:
    devices_inv = yaml.safe_load(f)

cisco3 = devices_inv["cisco4"]


net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())

running_config = net_connect.send_command("show run")

config_obj = CiscoConfParse(running_config.splitlines(), ignore_blank_lines=False)


#print(config_obj)

"""
Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
"""

intfs = config_obj.find_objects(r"^interface")

intfs_with_ip = list()

for intf in intfs:
    for child in intf.children:
        if "no ip address" in child.text:
            pass
        elif "ip address" in child.text:
            intf_with_ip = dict()
            intf_with_ip["Interface Line"] = intf.text
            intf_with_ip["IP Address Line"] = child.text
            intfs_with_ip.append(intf_with_ip)
        
pprint(intfs_with_ip)

net_connect.disconnect()

