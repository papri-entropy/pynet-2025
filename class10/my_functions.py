#!/usr/bin/env python

from netmiko import ConnectHandler

def ssh_command(a_device, show_command):
    print()
    print("#" * 40)
    remote_conn = ConnectHandler(**a_device)
    print(remote_conn.host)
    print("#" * 40)
    result = remote_conn.send_command_expect(show_command)
    remote_conn.disconnect()

    print(result)
    print("#" * 40)
    print()


def ssh_command2(a_device, show_command):
    print()
    print("#" * 40)
    remote_conn = ConnectHandler(**a_device)
    print(remote_conn.host)
    print("#" * 40)
    if show_command == "show ip arp":
        if remote_conn.host == "srx2.lasthop.io":
            result = remote_conn.send_command_expect("show arp")
        else:
            result = remote_conn.send_command_expect("show ip arp")

    else:    
        result = remote_conn.send_command_expect(show_command)

    remote_conn.disconnect()

    return result
