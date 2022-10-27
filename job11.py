
#!/usr/bin/env python3
from xml.dom   import minidom
doc = minidom.parse('domain.xml')
elements = doc.getElementsByTagName("column")
newlist = []
for element in elements:
    if element.getAttribute("name")  == "domain"
    newlist.append(element.childNodes[0].data)
    print(len(newlist))

