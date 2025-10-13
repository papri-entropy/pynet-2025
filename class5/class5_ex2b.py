#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


nxos_vars = {
    "nxos1_intf": "Ethernet1/1",
    "nxos1_ipv4": "10.1.100.1",
    "nxos1_mask": 24,
    "nxos1_local_as": 22,
    "nxos1_bgp_peer": "10.1.100.2",
    "nxos2_intf": "Ethernet1/1",
    "nxos2_ipv4": "10.1.100.2",
    "nxos2_mask": 24,
    "nxos2_local_as": 22,
    "nxos2_bgp_peer": "10.1.100.1",
    }



nxos_template_file = "class5_ex2b.j2"
template = env.get_template(nxos_template_file)
output = template.render(**nxos_vars)
print(output)
