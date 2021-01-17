'''
Guess an integer until you catch it.
'''
import random 
x = random.randint(0,30) 
while True: 
  guess = int(input('Guess the value of x: '))
  if guess == x: 
     print('You made it 😄')
     break 
  elif abs(guess - x) <= 2: 
     print("You're very close 😅")
  elif abs(guess - x) >= 8: 
     print("You're very far away 🙃")
  else:
     print('Try harder 🧐') 
