#!/usr/bin/python

print "Challenge 3"

with open ("input_text3.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

check_next = False
upp_let_count = 0
new_string = ""
first_four = False
for letter in data:
  if check_next:
    if not letter.isupper():
      print "String is ", new_string
    else:
      upp_let_count = 0
      new_string = ""
      first_four = False
      check_next = False
  if first_four == False:
    if (letter.isupper()) and (upp_let_count < 4):
      upp_let_count+=1
      new_string+=letter
    if not letter.isupper():
      if upp_let_count == 3:
        new_string+=letter
        upp_let_count =0
        first_four = True
      else:
        new_string = ""
        upp_let_count = 0
  else:
    if (letter.isupper()) and (upp_let_count < 3):
    	upp_let_count+=1
    	new_string+=letter
    	if upp_let_count == 3:
    	  check_next = True	
    else:
        upp_let_count = 0
        new_string = ""
        first_four = False
    	
#So the above was good enough to solve the problem, but gives a false positive where there
#are more than 3 capitals before the lower case letter.
