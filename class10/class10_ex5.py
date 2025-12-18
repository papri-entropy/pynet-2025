#!/usr/bin/env python

import time
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
from netmiko import ConnectHandler
from my_devices import device_list as devices
from my_functions import ssh_command2



def main():
    start_time = datetime.now()
    
    max_threads = 4

    # Use context manager to gracefully cleanup the pool

    with ProcessPoolExecutor(max_threads) as pool:
        
        future_list = []

        for a_device in devices:
            future = pool.submit(ssh_command2, a_device, "show version")
            future_list.append(future)


        # Process as completed

        for future in as_completed(future_list):
            print()
            print("#" * 40)
            print("Result: " + future.result())
            print()
            print("#" * 40)

            end_time = datetime.now()

            print(end_time - start_time)

    print("\nElapsed time: ", datetime.now() - start_time)

if __name__ == "__main__":
    main() 



