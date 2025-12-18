#!/usr/bin/env python

from datetime import datetime
import threading
from netmiko import ConnectHandler
from my_devices import device_list as devices
from my_functions import ssh_command



def main():
    """
    Use threads and Netmiko to connect to each of the devices. Execute
    show command on each device. Record the amount of time required to do this
    """
    start_time = datetime.now()

    for a_device in devices:
        my_thread = threading.Thread(target=ssh_command, args=(a_device, "show version"))

        my_thread.start()

    main_thread = threading.currentThread()
    for a_thread in threading.enumerate():
        if a_thread != main_thread:
            print(a_thread)
            a_thread.join()
    
    print("\nElapsed time: ", datetime.now() - start_time)


if __name__ == "__main__":
    main() 



