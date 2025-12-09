from lxml import etree


# Read the XML file in binary mode because it contains an encoding declaration

with open("show_version_nxos.xml", "rb") as f:
    xml_bytes = f.read()

# Parse the XML

root = etree.fromstring(xml_bytes)

# Print the namespce map

print(root.nsmap)

proc_board_id = root.find(".//{*}proc_board_id")

print(proc_board_id.text)


