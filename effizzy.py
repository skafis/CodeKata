#! /usr/bin/env python
#program that receives argument and checks if it is divisible by 3,5 or both

def effizy(item):
	#checking if argument is divisble by three
    div3=int(item)%3 
	#checking if argument is divisble by five
    div5=int(item)%5
    
    #checking if argument is divisble by both three and five
    if div3==0 and div5==0:
        print "FizzBuzz"
        
    elif div3==0:
	print "Fizz"
	
    elif div5==0:
	print "Buzz"
	
    else:
	print item
item = raw_input("Enter an argument:")
effizy(item)
