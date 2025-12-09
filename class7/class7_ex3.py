from pprint import pprint
import xmltodict


def xmlconverter(filename):
    xmlfile = open(filename)
    xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata)
    
    return my_xml


xml1 = xmlconverter("show_security_zones.xml")
xml2 = xmlconverter("show_security_zones_single_trust.xml")


#pprint(xml1)
#pprint(xml2)

print(type(xml1["zones-information"]["zones-security"]))
print(type(xml2["zones-information"]["zones-security"]))



def xmlconverter_v2(filename):
    xmlfile = open(filename)
    xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata, force_list={"zones-security": True})
    
    return my_xml

xml3 = xmlconverter_v2("show_security_zones_single_trust.xml")

print(type(xml3["zones-information"]["zones-security"]))



    


