# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy

dice = 6
again = True
results = []

print('random dice roller')

while again:
    R = random.randint(1,dice) 
    print(R)
      
    results.append(R)
      
    i=input("roll again? Y/n ")
    
    again = False 
    if i in ['y','Y','yes','Yes']:
        again = True
    else:
        print(results)
  
        
        
        
