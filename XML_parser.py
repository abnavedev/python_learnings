# extract data from XML

# XML is used to for data presentataion , used to send data between client and servers

# Parsing means to read info and split it into pieces by identifying parts 
# modile ElementTree

import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')

root = tree.getroot()


