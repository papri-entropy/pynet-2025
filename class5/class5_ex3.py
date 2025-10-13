#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

bgp_vrf_vars = {
    "ipv4_enabled": True,
    "ipv6_enabled": True,
    "vrf_name": "blue",
    "rd_number": "100:1"
    }


bgp_vrf_template_file = "class5_ex3.j2"
template = env.get_template(bgp_vrf_template_file)
output = template.render(**bgp_vrf_vars)

print(output)
