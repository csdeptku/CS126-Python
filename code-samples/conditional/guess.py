'''
Integer guessing game.
'''
import random 
x = random.randint(0,30) 
guess = int(input('Guess the value of x: ')) 
if guess == x: 
   print('You made it 😄')
elif abs(guess - x) <= 2: 
   print("You're very close 😅")
elif abs(guess - x) >= 8: 
   print("You're very far away 🙃")
else:
   print('Try harder 🧐') 
