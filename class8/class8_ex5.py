from jnpr.junos import Device
from pprint import pprint
from jnpr_devices import srx2
from lxml import etree

if __name__ == "__main__":

    srx2_device = Device(**srx2)

    srx2_device.open()  

    show_ver = srx2_device.rpc.get_software_information()
    
    pprint(etree.tostring(show_ver, encoding="unicode"))


    show_intf_terse = srx2_device.rpc.get_interface_information(terse=True)

    pprint(etree.tostring(show_intf_terse).decode())

    xml_out = srx2_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)

    print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

    










