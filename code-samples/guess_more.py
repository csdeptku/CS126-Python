'''
Guess an integer until you catch it.
'''
import random 
x = random.randint(0,30) 
i = 0
j = 0 
max_guesses = 5
while i < max_guesses: 
  guess = int(input('Guess the value of x: '))
  i+=1
  if guess == x: 
     print('You made it 😄')
     break 
  elif abs(guess - x) <= 2: 
     print("{}: You're very close 😅".format(i))
     i-=1
  elif abs(guess - x) >= 8: 
     print("{}: You're very far away 🙃".format(i))
  else:
     print('{}: Try harder 🧐'.format(i)) 
   
  j+=1 
print('You had {} attempts and the number was {}.'.format(j,x)) 
