from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

junos_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())

junos_device.open()

pprint(junos_device.facts)

print("#" * 20)

print(junos_device.facts["hostname"])
