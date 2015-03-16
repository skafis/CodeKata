#! /usr/bin/env python
#finding the 10001st number in a prime
primenum = []
def isPrime(x):
  for i in primesnum:
      if(x % i == 0):
          return 0
  return 1
  
primeCount = 0
i = 2;
while(primeCount <= 10001):
  if(isPrime(i)):
      print i
      primenum.append(i)
      primeCount = primeCount + 1
      if(primeCount == 10001):
          print i
          break
  i = i + 1
