# extract data from XML

# XML is used to for data presentataion , used to send data between client and servers

# Parsing means to read info and split it into pieces by identifying parts 
# Parsing can be done using 2 modules 
# tElementTree i.e xml.etree.ElementTree module and Minidom (Minimal DOM Implementation)


# xml.etree.ElementTree Module:
#  format XML data in a tree structure
import xml.etree.ElementTree as ET


# Using parse() function:

tree = ET.parse('sample.xml')

root = tree.getroot() #getroot( returns the root element


# edureka