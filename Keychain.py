# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:21:36 2021

@author: Forensics Laptop
"""

import xml.etree.ElementTree as ET
import base64

filename = "d:/test/keychain.plist"
tree = ET.parse(filename)
root = tree.getroot()

valuesList = []
for values in root.findall(".//data"):
    if len(values.text) % 4 == 0: #base64 strings should be divisible by 4
           try:
               values.text = str(base64.b64decode(values.text))
               
           except Exception:
               pass

for values in root.findall(".//data"):
    if values.text[0:2] == "b'":
        values.text = str(values.text[2:-1])

tree.write(filename + "-edited.xml")
