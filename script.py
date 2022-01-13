import csv
import xml.etree.cElementTree as ET

import_dict = {}

with open('../../tmp/phones.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for n, row in enumerate(csv_reader):
        if not n:
            continue
            
        extension, building, name = row
        if building not in import_dict:
            import_dict[building] = list()
        import_dict[building].append((name, extension))

# Figure out version and encoding

root = ET.Element("YealinkIPPhoneBook")
title = ET.SubElement(root, "Title").text= "Yealink"

for key, values in import_dict.items():
    doc = ET.SubElement(root, "Menu", Name=key)
    for value in values:
        ET.SubElement(doc, "Unit", Name=value[0], Phone1=value[1], Phone2="", Phone3="", default_photo="Resource:")


tree = ET.ElementTree(root)
tree.write("../../var/www/html/ph-directory/min201directory.xml", encoding = "UTF-8", xml_declaration = True)
