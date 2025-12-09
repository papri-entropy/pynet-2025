import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")

print(etree.tostring(output).decode())

interface = output.find(".//interface")

state = output.find(".//state")

mtu = output.find(".//eth_mtu")

print(f"Interface: {interface.text}; State: {state.text}; MTU: {mtu.text}")

cmds = [
    "show system uptime",
    "show system resources",
]

output = device.show_list(cmds)

for entry in output:
    print(etree.tostring(entry).decode())
    input("Hit enter to continue: ")

config_cmds = [
    "interface loopback 104",
    "description 104",
    "interface loopback 144",
    "description 144"
]

output = device.config_list(config_cmds)

for entry in output:

    print(etree.tostring(entry).decode())


    
