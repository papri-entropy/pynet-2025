#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
import yaml
from pprint import pprint


password = getpass()

filename = ".netmiko.yml"

with open(filename) as f:
    devices_inv = yaml.safe_load(f)

cisco3 = devices_inv["cisco3"]


net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())


net_connect.disconnect()

