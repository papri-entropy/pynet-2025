#!/usr/bin/env python

import json
from pprint import pprint


filename = "class3_ex3.json"

with open(filename) as f:
    nexus_data = json.load(f)

"""
Ethernet2/2
{'ipv4': {'2.2.2.2': {'prefix_length': 27}, '3.3.3.3': {'prefix_length': 25}}}
"""

ipv4_list = list()
ipv6_list = list()

for k, v in nexus_data.items():
    for x, y in v.items():
        for m, n in y.items():
            if x =="ipv4":
                ipv4_list.append(m + "/" + str(n["prefix_length"]))
            elif x =="ipv6":
                ipv6_list.append(m + "/" + str(n["prefix_length"]))

print(ipv4_list)
print(ipv6_list)
            
        
        
         

