#!/usr/bin/python

print "Challenge 4"

import urllib

nothings = "12345"

for x in range(0, 1000):
  url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothings
  response = urllib.urlopen(url)
  html = response.read()
  nothings = html[-5:]
  if nothings == ".html": 
    print html
    break
  print nothings

print "finished"