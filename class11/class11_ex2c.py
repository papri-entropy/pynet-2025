#!/usr/bin/env python

import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":

    # url = https://netbox.lasthop.io/api/

    url = "https://netbox.lasthop.io/api/dcim/"
    http_headers = {"accept": "application/json;"}
    response = requests.get(url, headers=http_headers, verify=False)

    print()
    print("#" * 40)
    pprint(response.json())
    print()
    print("#" * 40)
