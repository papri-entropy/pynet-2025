#!/usr/bin/env python

from pprint import pprint


arp = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
	"""


intf_list = []

arp = arp.splitlines()[2:-1]


for data in arp:
    intf_dict = {}

    data = data.split()

    ip_addr = data[1]
    mac_addr = data[3]
    intf = data[5]

    intf_dict["mac_addr"] = mac_addr
    intf_dict["ip_addr"] = ip_addr
    intf_dict["interface"] = intf

    intf_list.append(intf_dict)


pprint(intf_list)
    



