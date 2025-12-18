#!/usr/bin/env python

import os
import json
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":


    ip_addr_url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/47/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json"
    http_headers["accept"] = "application/json"
    http_headers["Authorization"] = f"Token {token}"

    response = requests.delete(ip_addr_url, headers=http_headers, verify=False)

    if response.ok:
        print("IP addr deleted successfully")




