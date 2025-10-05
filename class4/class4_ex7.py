#!/usr/bin/env python

from pprint import pprint
import textfsm

template_file = "class4_ex2.tpl"
template = open(template_file)

with open("show_int_status.txt") as f:
    raw_text_data = f.read()


re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

int_status = list()

for entry in data:
    entry_dict = dict()
    entry_dict["DUPLEX"] = entry[3]
    entry_dict["PORT_NAME"] = entry[0]
    entry_dict["PORT_TYPE"] = entry[5]
    entry_dict["SPEED"] = entry[4]
    entry_dict["STATUS"] = entry[1]
    entry_dict["VLAN"] = entry[2]

    int_status.append(entry_dict)

pprint(int_status)
    
    



