#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import yaml
from pprint import pprint
from netmiko import ConnectHandler
import my_devices



env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


nxos1_vars = {
    "nxos1_intf": "Ethernet1/1",
    "nxos1_ipv4": "10.1.100.1",
    "nxos1_mask": 24,
    "nxos1_local_as": 22,
    "nxos1_bgp_peer": "10.1.100.2",
    }

nxos2_vars = {
    "nxos2_intf": "Ethernet1/1",
    "nxos2_ipv4": "10.1.100.2",
    "nxos2_mask": 24,
    "nxos2_local_as": 22,
    "nxos2_bgp_peer": "10.1.100.1",
    }



nxos1_template_file = "class5_ex2c_nxos1.j2"
nxos1_template = env.get_template(nxos1_template_file)
nxos1 = nxos1_template.render(**nxos1_vars)
print(nxos1)

nxos2_template_file = "class5_ex2c_nxos2.j2"
nxos2_template = env.get_template(nxos2_template_file)
nxos2 = nxos2_template.render(**nxos2_vars)
print(nxos2)

nxos_devices = [my_devices.nxos1, my_devices.nxos2]


for device in nxos_devices:

    if device['host'] == 'nxos1.lasthop.io':

        net_connect = ConnectHandler(**device)
        print(net_connect.find_prompt())

        config = net_connect.send_config_set(nxos1.splitlines())
        print(config)

        save_config = net_connect.save_config()
        print(save_config)
        
        ping = net_connect.send_command_timing("ping 10.1.100.2")

        print("\n")
        print(ping)
        print("\n")

        if "5 packets transmitted, 5 packets received" in ping:
            print("PING NXOS2 NEIGH OK")
        else:
            print("PING FAILED")
        
        show_bgp = net_connect.send_command("sh ip bgp neighbors 10.1.100.2", use_textfsm=True)

        print("*" * 40)
        print(show_bgp) 
        print("*" * 40)

        if show_bgp[0]["bgp_state"] == "Established":
            print("BGP ESTABLISHED STATE")
        else:
            print("BGP NOT OK")



    elif device['host'] == 'nxos2.lasthop.io':

        net_connect = ConnectHandler(**device)
        print(net_connect.find_prompt())

        config = net_connect.send_config_set(nxos2.splitlines())
        print(config)

        save_config = net_connect.save_config()
        print(save_config)

        ping = net_connect.send_command_timing("ping 10.1.100.1")

        print("\n")
        print(ping)
        print("\n")

        if "5 packets transmitted, 5 packets received" in ping:
            print("PING NXOS2 NEIGH OK")
        else:
            print("PING FAILED")

        show_bgp = net_connect.send_command("sh ip bgp neighbors 10.1.100.1", use_textfsm=True)

        print("*" * 40)
        print(show_bgp) 
        print("*" * 40)

        if show_bgp[0]["bgp_state"] == "Established":
            print("BGP ESTABLISHED STATE")
        else:
            print("BGP NOT OK")

net_connect.disconnect()

