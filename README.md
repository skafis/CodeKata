# CodeKata
#! /usr/bin/env python
#palindrome.py
#Program for reversing a string

#inputing the string
name = raw_input("enter your the name to be reverserd.")

#reversing the string
mystr = name [::-1]

if name == "": #check is if the string is null
	print "null"
elif name == mystr: #check if the string is the same as returned value
	print "true"
else:
	print mystr; #print the reverse of the string
	
