#!/usr/bin/env python

from pprint import pprint
from getpass import getpass
import yaml
import pyeapi

import my_funcs


password = getpass()

filename = "pyeapi_conn.yml"

arista4 = my_funcs.yaml_reader(filename)["arista4"]
arista4["password"] = password


connection = pyeapi.client.connect(**arista4)

device = pyeapi.client.Node(connection)

show_route = device.enable("show ip route")


for k, v in show_route[0]["result"]["vrfs"]["default"]["routes"].items():
    if v['routeType'] == 'static':
        print(f"{k} is route type {v['routeType']} with nexthop {v['vias'][0]['nexthopAddr']}")
    elif  v['routeType'] == 'connected':
        print(f"{k} is route type {v['routeType']}")


