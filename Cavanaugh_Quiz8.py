# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:40:22 2022

@author: User
"""

user_list = []
threshold_low = int(input('Enter lower boundary: '))
threshold_high = int(input('Enter higher boundary: '))
num = int(input('Enter non-negative number or a negative number when you\'re done: '))
count = 0

while num >=0:
        user_list.append(num)
        num=int(input('Enter non-negative number or a negative number when you\'re done: '))

user_list.sort()
     
    
print('the numbers that are between', threshold_low, 'and', threshold_high, 'and are multiples of 3 are')
for i in user_list:
        if (i >= threshold_low and i <= threshold_high and i%3==0):
                print(i, end='')
                
        
        

#for i in range(threshold_low, threshold_high+1):
    #if i%3==0:
            #count+=1
#print(i, end='')