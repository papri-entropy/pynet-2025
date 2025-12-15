#!/usr/bin/env python

from getpass import getpass
from napalm import get_network_driver

password = getpass()

cisco3 = {
  "device_type": "ios",
  "hostname": "cisco3.lasthop.io",
  "username": "pyclass",
  "password": password 
}

arista1 = {
  "device_type": "eos",
  "hostname": "arista1.lasthop.io",
  "username": "pyclass",
  "password": password
}

nxos1 = {
  "device_type": "nxos",
  "hostname": "nxos1.lasthop.io",
  "username": "pyclass",
  "password": password,
  "optional_args": {"port": 8443}
}

def napalm_conn(device, device_type):
    driver = get_network_driver(device_type)
    target_device = driver(**device)

    target_device.open()
    
    return target_device
