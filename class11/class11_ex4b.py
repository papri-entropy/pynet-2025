#!/usr/bin/env python

import os
import json
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":


    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json"
    http_headers["accept"] = "application/json"
    http_headers["Authorization"] = f"Token {token}"

    post_data = {"address": "192.0.2.244/32"}

    response = requests.post(url, headers=http_headers, data=json.dumps(post_data), verify=False)

    print()
    print("#" * 40)
    my_ip_add_id = response.json()["id"]
    print(my_ip_add_id)
    print()
    print("#" * 40)

    ip_addr_url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{my_ip_add_id}/"

    get_response = requests.get(ip_addr_url, headers=http_headers, verify=False)
    pprint(get_response.json())

