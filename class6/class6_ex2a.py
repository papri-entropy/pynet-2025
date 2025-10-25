#!/usr/bin/env python

from pprint import pprint
from getpass import getpass
import yaml
import pyeapi

password = getpass()

filename = "pyeapi_conn.yml"

with open(filename) as f:
    devices_inv = yaml.safe_load(f)

arista4 = devices_inv["arista4"]
arista4["password"] = password


connection = pyeapi.client.connect(**arista4)

device = pyeapi.client.Node(connection)

arp_output = device.enable("show ip arp")


arp_mapping = dict()

for arp in arp_output[0]["result"]["ipV4Neighbors"]:
    arp_mapping[arp["address"]] = arp["hwAddress"]


pprint(arp_mapping)
