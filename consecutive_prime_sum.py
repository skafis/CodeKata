#! /usr/bin/env python
#program calculating the consecutive prime number

import prime
p=prime.genprimes(1000)
prms = [i for i in p]
found = []
for prm in prms:
	count = 0
	p=prm
	temp = []
	for a in prms:
		p-=a
		temp.append(a)
		count += 1
		if p==0:
			print prm, '\t', count,
