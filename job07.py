#!/usr/bin/env python3 
i = 1
n = 1
while i <= 100 & n <= 100:
   print(i)
   if  i == 3*n:
     print("Fizz")
   if i == 5*n:
     print("Buzz")
   if i == 3*5*n:
     print("Fizzbuzz")
