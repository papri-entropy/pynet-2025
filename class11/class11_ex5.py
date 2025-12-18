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

    ip_addr_put = dict()
    ip_addr_put["address"] = "192.0.2.244/32"
    ip_addr_put["description"] = "COSMIN"

    response = requests.put(ip_addr_url, headers=http_headers, data=json.dumps(ip_addr_put), verify=False)

    print()
    print("#" * 40)
    pprint(response.status_code)
    print()
    print("#" * 40)
    pprint(response.json())
    print()
    print("#" * 40)



