#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

#password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
	"session_log": "netmiko_ex4_cisco3.txt",
    "fast_cli": True
}



net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())

cfg = [
   "ip name-server 1.1.1.1",
	"ip name-server 1.0.0.1",
	"ip domain-lookup"

]

config = net_connect.send_config_set(cfg)
print(config)


ping = net_connect.send_command_timing("ping google.com")

print("\n")
print(ping)
print("\n")

if "Success rate is 100 percent" in ping:
    print("DNS working as expected")



net_connect.disconnect()
