#!/usr/bin/env python
#Simple program to check if a number is armstrong number

number =raw_input ("Enter three digit number:") 

#finding the sum of the individual numbers
sum = int(number[0])**3 + int(number[1])**3 + int(number[2])**3 

#comparing if the sum equals to the inputed number
if sum == int(number):
	print "true"
else: 
	print "false"
		  
