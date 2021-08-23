'''
Write a program to receive a list of numbers from the user.
Calculate and print the average of the received numbers up to 
two decimal places. Assume the user enters each number
separated by a space. 
'''
S = input()
S = S.split(' ')
L = list(map(eval, S)) 
avg = round(sum(L)/len(L), 2)
print(avg)
