#!/usr/bin/env python

import json
from pprint import pprint


filename = "class3_ex4.json"

with open(filename) as f:
    arista_arp = json.load(f)


arista_arp = arista_arp["ipV4Neighbors"]

"""
[{'address': '172.17.17.1',
  'age': 0,
  'hwAddress': 'dc38.e111.97cf',
  'interface': 'Ethernet45'},
 {'address': '172.17.16.1',
  'age': 0,
  'hwAddress': '90e2.ba5c.25fd',
  'interface': 'Ethernet36'}]"
"""


def arp_transform(arp_data):
    
    arp_dict = dict()

    for element in arista_arp:
        address = element["address"]
        mac = element["hwAddress"]
        arp_dict[address] = mac
    
    return arp_dict



pprint(arp_transform(arista_arp))
