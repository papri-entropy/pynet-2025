#!/usr/bin/env python

from pprint import pprint
from my_devices import cisco3, arista1
from my_devices import napalm_conn


switches = [cisco3, arista1] 



for switch in switches:
    print(switch)

for switch in switches:
    device_type =  switch.pop("device_type")

    conn = napalm_conn(switch, device_type) 
    pprint(conn.device)

    pprint(conn.get_facts())
    
    print(device_type)
