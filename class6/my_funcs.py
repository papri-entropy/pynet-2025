#!/usr/bin/env python

import yaml

def yaml_reader(filename):
	
    with open(filename) as f:
        devices_inv = yaml.safe_load(f)

    return devices_inv

def arp_output(arp_output):
	
    arp_mapping = dict()

    for arp in arp_output[0]["result"]["ipV4Neighbors"]:
        arp_mapping[arp["address"]] = arp["hwAddress"]
	
    return arp_mapping



