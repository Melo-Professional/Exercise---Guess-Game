# -*- coding: utf-8 -*-
"""GuessGameExercise.ipynb
By Melo
melo@meloprofessional.com
"""

import random
import math
print(f'Guessing Game')
print(f'You need to guess a number from a range you choose')
print(f'Ready?')
range_min, range_max = [int(x) for x in input("Range to draw (n1-n2): ").split('-')]
max_tries = math.ceil(math.log2(abs(range_max+2-range_min)))
print ("You has",max_tries,"guesses")
secret_number = random.randrange((range_min),(range_max+1))
amount_tries = 1
stupid = False
old_guess = set()
current_guess = int(input(f'1/{max_tries} - Guess the number : '))
old_guess = set(list(old_guess) + list([current_guess]))
while amount_tries <= max_tries:
  if current_guess == secret_number:
    print("You Rocks!")
    break
  if stupid != True:
    if current_guess < secret_number:
      print(str(current_guess) + " is too low")
    else:
      print(str(current_guess) + " is too HIGH")
  if amount_tries < max_tries:
    amount_tries+=1
    current_guess = int(input(f'{amount_tries}/{max_tries} - Try another: '))
    stupid = False
    if current_guess in (old_guess):
      stupid = True
      print("You'd already tried it...")
    old_guess = set(list(old_guess) + list([current_guess]))
  else:
    print("You lose! The number was:", secret_number)
    break

