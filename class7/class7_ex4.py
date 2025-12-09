from lxml import etree



zones_information = """
<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>
"""


my_xml = etree.fromstring(zones_information)


first_zone_sec = my_xml.find("zones-security")

print("Find tag of the first zones-security element")
print("--------------------")
print(first_zone_sec.tag)
print("Find tag of all child elements of the first zones-security element")
print("--------------------")

for child in first_zone_sec:
    print(child.tag)

"""
for child in first_zone_sec.getchildren():
    print(child.tag)
"""

zone_sec_zonename = my_xml.find(".//zones-security-zonename")

print(zone_sec_zonename.text)

zones_sec = my_xml.findall(".//zones-security")

for zone in zones_sec:

    print(zone[0].text)


