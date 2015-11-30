#!/usr/bin/python

from string import maketrans

print "Challenge 1"
# Used http://www.tutorialspoint.com/python/string_maketrans.htm for reference
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
transtab = maketrans(intab, outtab)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print str.translate(transtab)
str2 = "map"
print str2.translate(transtab)
