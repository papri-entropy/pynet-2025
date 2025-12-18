#!/usr/bin/env python

import time
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
from netmiko import ConnectHandler
from my_devices import device_list as devices
from my_functions import ssh_command2
from itertools import repeat




def main():
    start_time = datetime.now()
    
    max_threads = 4

    # Use context manager to gracefully cleanup the pool

    with ProcessPoolExecutor(max_threads) as pool:

        results_generator = pool.map(ssh_command2, devices, repeat("show ip arp"))

        # Results generator
        for result in results_generator:

            print(result)
            end_time = datetime.now()
            print(end_time - start_time)

    print("\nElapsed time: ", datetime.now() - start_time)

if __name__ == "__main__":
    main() 



