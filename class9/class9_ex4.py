#!/usr/bin/env python

from pprint import pprint
from my_devices import cisco3, arista1, nxos1
from my_functions import open_napalm_connection
from my_functions import create_backup
from my_functions import create_checkpoint


switches = [nxos1]



for switch in switches:
    print(switch)

for switch in switches:
    device_type =  switch.pop("device_type")

    conn = open_napalm_connection(switch, device_type) 

    print(conn)
    
    checkpoint = create_checkpoint(conn)

    print()
    print(">>>Load config changes (replace)")
    conn.load_replace_candidate(filename=f"{conn.hostname}_v2_checkpoint")

    print(conn.compare_config())

    print()
    print(">>>Discarding config changes (replace)")


    conn.discard_config()
    
    print(conn.compare_config())
