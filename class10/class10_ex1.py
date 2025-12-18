#!/usr/bin/env python

from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list as devices

def show_command(a_device, show_command):
    print()
    print("#" * 40)
    remote_conn = ConnectHandler(**a_device)
    print(remote_conn.host)
    print()
    print("#" * 40)
    result = remote_conn.send_command_expect(show_command)
    remote_conn.disconnect()

    return result


for a_device in devices:
    print(show_command(a_device, "show version"))


