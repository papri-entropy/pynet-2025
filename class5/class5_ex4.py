#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


vrfs = {
        "blue":
        {
        "name": "blue",
        "rd" : "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True
        },
        "green":
        {
        "name": "green",
        "rd" : "200:2",
        "ipv4_enabled": True,
        "ipv6_enabled": True
        },
        "red":
        {
        "name": "red",
        "rd" : "300:3",
        "ipv4_enabled": True,
        "ipv6_enabled": True
        },
        "yellow":
        {
        "name": "yellow",
        "rd" : "400:4",
        "ipv4_enabled": True,
        "ipv6_enabled": True
        },
        "brown":
        {
        "name": "brown",
        "rd" : "500:5",
        "ipv4_enabled": True,
        "ipv6_enabled": True
        },
        }

template_vars = {
        "vrfs": vrfs,
}

bgp_vrf_template_file = "class5_ex4.j2"
template = env.get_template(bgp_vrf_template_file)
output = template.render(**template_vars)

print(output)
