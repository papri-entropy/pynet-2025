#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""


bgp_obj = CiscoConfParse(bgp_config.strip().splitlines(), ignore_blank_lines=False)

bgp_neigh = bgp_obj.find_objects(r"router bgp 44")

bgp_neigh = bgp_neigh[0]

bgp_list = []

for neigh in bgp_neigh.children:
    if "neighbor" in neigh.text:
        neighbor = neigh.text.split()[1]
        #print(neighbor)
        
        remote_as = neigh.re_search_children(r"remote-as")[0].text.split()[1]
        #print(remote_as)
        
        bgp_list.append((neighbor, remote_as))

print("BGP Peers:")
print(bgp_list)




