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

show_arp = device.enable("show ip arp")


pprint(my_funcs.arp_output(show_arp))


