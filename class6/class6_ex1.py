#!/usr/bin/env python
from pprint import pprint

import pyeapi
from getpass import getpass
password = getpass()

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=password,
    port="443",
)

device = pyeapi.client.Node(connection)
arp_output = device.enable("show ip arp")


arp_mapping = dict()

for arp in arp_output[0]["result"]["ipV4Neighbors"]:
    arp_mapping[arp["address"]] = arp["hwAddress"]


pprint(arp_mapping)
