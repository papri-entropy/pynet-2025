#!/usr/bin/env python

import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait
from netmiko import ConnectHandler
from my_devices import device_list as devices
from my_functions import ssh_command2



def main():
    start_time = datetime.now()
    
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for a_device in devices:

        future = pool.submit(ssh_command2, a_device, "show version")
        future_list.append(future)

    # Waits until all the pending threads are done
    wait(future_list)

    for future in future_list:
        print()
        print("#" * 40)
        print("Result: " + future.result())
        print()
        print("#" * 40)

    end_time = datetime.now()

    print(end_time - start_time)

if __name__ == "__main__":
    main() 



