# What is XML? simailar to HTML

# used to for data presentataion
# used to send data between client and servers

# Parsing ? to read info and split it , extract it 
# Parsing can be done using 2 modules  in python
# ElementTree i.e xml.etree.ElementTree module 
# Minidom (Minimal DOM Implementation)


# Parsing using xml.etree.ElementTree Module:
#  It format XML data in a tree structure
# It has properties Tag Attribute Test String Tail String CHild ELEments

import xml.etree.ElementTree as ET

# there are 2 ways
# parse() function: XML file
# fromstring() - If XML is given in string form

# using parse function

tree = ET.parse('sample.xml')  
# print(type(tree))

xml_root = tree.getroot() #getroot( returns the root element

print(xml_root)

print(xml_root.tag) # get the root tag by using the ‘tag’ object
## roottag is metadata in the sample

print(xml_root.attrib) 
# tags has attributes as dictionary
# root tag has no attributes so empty dicionary


# To find the element of interest 

# root has child 
# to get child tag and attributes
# xml_root[0].tag 
# xml_root[0].attrib

# To get to  all first-child tags of the root,
print("##########")

for i in xml_root[0] :
    print(i.tag,"-->", i.attrib)

# here first food - first child-  attributes and tags.

# to get info of the the first food item, 

for i in xml_root[0] :
    print(i.text)


# tp get all the items  with particular price
# use get()

for i in xml_root.findall('food') : # search for all occurance of food
    item = i.find('item').text
    price = i.find('price').text
    print(item,price)

# Adding data to XML
# use set()

