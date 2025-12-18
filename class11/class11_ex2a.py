#!/usr/bin/env python

import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":

    # url = https://netbox.lasthop.io/api/

    url = "https://netbox.lasthop.io/api/"

    response = requests.get(url, verify=False)
    print()
    print("#" * 40)
    print(response.status_code)
    print()
    print("#" * 40)
    print(response.text)
    print()
    print("#" * 40)
    print(response.json())
    print()
    print("#" * 40)
    print(response.headers)
    print()
    print("#" * 40)
