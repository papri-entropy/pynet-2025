#!/usr/bin/env python

import os
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":


    url = "https://netbox.lasthop.io/api/dcim/devices/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {"accept": "application/json;"}
    http_headers["Authorization"] = f"Token {token}"

    response = requests.get(url, headers=http_headers, verify=False)

    print()
    print("#" * 40)
    for device in response.json()["results"]:
        print(device["display"])
    print()
    print("#" * 40)
