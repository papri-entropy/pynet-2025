#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nexus1 =  {
    "host": "nxos1.lasthop.io", 
    "username":"pyclass", 
    "password": password, 
    "device_type": "cisco_nxos",
}

nexus2 =  {
    "host": "nxos2.lasthop.io", 
    "username":"pyclass", 
    "password": password, 
    "device_type": "cisco_nxos",
}

devices = [nexus1, nexus2]

for device in devices:
    net_connect = ConnectHandler(**device)

    print(net_connect.find_prompt())
    
    config = net_connect.send_config_from_file(config_file="class2_netmiko_ex5_nexus_vlans.txt")
    
    print(config)

    save_config = net_connect.save_config()

    print(save_config)






net_connect.disconnect()
