#!/usr/bin/env python

import yaml
from pprint import pprint


devices = [
	{
  "device_type": "arista_eos",
  "host": "arista1.lasthop.io",
  "username": "superuser",
  "password": "superpass"
	},
	{
  "device_type": "arista_eos",
  "host": "arista2.lasthop.io",
  "username": "superuser",
  "password": "superpass"
	},
	{
  "device_type": "arista_eos",
  "host": "arista3.lasthop.io",
  "username": "superuser",
  "password": "superpass"
	},
	{
  "device_type": "arista_eos",
  "host": "arista4.lasthop.io",
  "username": "superuser",
  "password": "superpass"
	}
]


pprint(devices)


filename = "outfile.yml"

with open(filename, "wt") as f:
    yaml.dump(devices, f, default_flow_style=False)


