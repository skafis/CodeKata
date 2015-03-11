#! /usr/bin/env python
#Bubblesort.py
#program that performs a bubble sort
def bubbleSort (alist):
	for number in range (len(alist)-1,0,-1):
		for i in range (number):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1]=temp
alist = [79,34,67,87,58,92,45,77,16,27,19]
bubbleSort(alist)
print (alist)				
