#!/usr/bin/env python

from napalm import get_network_driver


def open_napalm_connection(device, device_type):
    driver = get_network_driver(device_type)
    target_device = driver(**device)

    target_device.open()

    return target_device

def create_backup(napalm_conn_obj):
    
    backup_config = napalm_conn_obj.get_config("running")["running"]


    with open(f"{napalm_conn_obj.hostname}_backup.txt", "w") as f:
        f.write(backup_config)
 

    return backup_config

def create_checkpoint(napalm_conn_obj):
    
    nxos_checkpoint = napalm_conn_obj._get_checkpoint_file()


    with open(f"{napalm_conn_obj.hostname}_checkpoint", "w") as f:
        f.write(nxos_checkpoint)
 

    return nxos_checkpoint

    
    
