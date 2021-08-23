'''
A simple program to print an answer based on the user's answer.
'''

ans = input('How are you?') 

if ans.find('good') > -1 or ans.find('fine') > -1 or ans.find('ok') > -1: 
  print('Great!')
else:
  print('Feel better tomorrow.')
