#!/usr/bin/env python

from pprint import pprint
from my_devices import cisco3, arista1
from my_functions import open_napalm_connection
from my_functions import create_backup


switches = [cisco3, arista1] 



for switch in switches:
    print(switch)

for switch in switches:
    device_type =  switch.pop("device_type")

    conn = open_napalm_connection(switch, device_type) 

    print(conn)
    
    print()
    print(">>>Load comnfig change (merge)")
    conn.load_merge_candidate(filename=f"{conn.hostname}-loopbacks")

    print(conn.compare_config())

    print(">>>Commiting config change (merge)")

    conn.commit_config()
    
    print(conn.compare_config())
