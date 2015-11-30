#!/usr/bin/python

import re
print "Challenge 2"

with open ("input_text.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

new_data = re.sub(r'\W+', '', data)
new_data = new_data.replace("_","")
print new_data

#The above was my first stab at it, after eyeballing the hash to see it was letters that were rare.  A better way (shown in the examples) would be:

for a in data:
    l = data.count(a)
    if l < 20:
        print a, ":", l
