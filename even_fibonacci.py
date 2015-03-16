#! /usr/bin/env python
#printing the sum of the even Fibonacci numbers

n= int(raw_input("enter your number"))
sumeven=0
# Defining the Fibonacci function
def fib(n): 
	a,b = 0,1 #first numbers of the sequence 
	while 1:
		yield a
		a,b = b,a+b #generator for the next number in the sequence
a = fib(n)

for i in range(n):
	b= a.next() #get the next number in the sequence
	if b<=4000000: #check if value returned exceeds 4 million
		if b % 2 == 0:
			sumeven +=b #calculate the sum of even numbers
		print "%d,%d"%(b,sumeven)
