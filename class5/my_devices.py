#!/usr/bin/env python

from getpass import getpass

password = getpass()

nxos1 = {
  "device_type": "cisco_nxos",
  "host": "nxos1.lasthop.io",
  "username": "pyclass",
  "password": password,
  "port": 22
}

nxos2 = {
  "device_type": "cisco_nxos",
  "host": "nxos2.lasthop.io",
  "username": "pyclass",
  "password": password,
  "port": 22
}
