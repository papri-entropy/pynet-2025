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


    print(f'{switch["hostname"]} ARP TABLE')
    pprint(conn.get_arp_table())

    try:
        print(f'{switch["hostname"]} NTP PEERS')
        pprint(conn.get_ntp_peers())
    except NotImplementedError:
        print(f'{switch["hostname"]} does not support get_ntp_peers()')

    
    config_backup = create_backup(conn)

    print(config_backup)
