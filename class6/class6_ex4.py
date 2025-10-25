#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from pprint import pprint
from getpass import getpass
import yaml
import pyeapi

import my_funcs

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

password = getpass()

filename = "pyeapi_arista.yml"

arista1 = my_funcs.yaml_reader(filename)["arista1"]
arista2 = my_funcs.yaml_reader(filename)["arista2"]
arista3 = my_funcs.yaml_reader(filename)["arista3"]
arista4 = my_funcs.yaml_reader(filename)["arista4"]
aristas = [arista1, arista2, arista3, arista4]

for arista in aristas:
    arista["password"] = password

    connection = pyeapi.client.connect(**arista)

    device = pyeapi.client.Node(connection)

    #pprint(arista)

    arista_vars = arista['data']

    arista_template_file = 'class6_ex4.j2'
    template = env.get_template(arista_template_file)
    config_loopbacks = template.render(**arista_vars)
    config_loopbacks = config_loopbacks.splitlines()

    config_push = device.config(config_loopbacks)
    print(config_push)


    intf_brief = device.enable("show ip interface brief")
    pprint(intf_brief[0]['result']['interfaces'])

"""
    you could also create arista_vars in this manner if your input keys need to be different for some reason

    arista_vars = dict()
    arista_vars['intf_name'] = arista['data']['intf_name']
    arista_vars['intf_ip'] = arista['data']['intf_ip']
    arista_vars['intf_mask'] = arista['data']['intf_mask']
"""
