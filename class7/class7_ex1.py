from lxml import etree


show_security_zones = """
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

my_xml = etree.fromstring(show_security_zones.strip())

print(my_xml)

print(type(my_xml))

xml_to_string = etree.tostring(my_xml).decode()

print(xml_to_string)



xml_data = etree.parse("show_security_zones.xml")

xml_data = xml_data.getroot()

print(xml_data.tag)

print(len(xml_data.getchildren()))

print(xml_data.getchildren()[0].tag)

print(xml_data[0].tag)

trust_zone = xml_data[0]


print(trust_zone.getchildren()[0])
print(trust_zone.getchildren()[0].text)


for child in trust_zone.getchildren():
    print(child.tag)
