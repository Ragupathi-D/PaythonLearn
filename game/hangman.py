import os
import random

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']

question = random.choice(fruits)
clear = lambda: os.system('clear')
correct = 0
totalChance = 5
leterLength = len(question)
fill = ['_' for _ in range(leterLength)]
checkWords = [question[i] for i in range(0, leterLength)]
while(leterLength != correct and totalChance != 0):
  print(f"Please find the word : {','.join(fill)}")
  print(f"Your total chance is {totalChance}")
  userInput = input('Please enter the word : ').lower()
  indexes = [ i for i in range(len(checkWords)) if(checkWords[i] == userInput) ]
  if(len(indexes) == 0 or userInput == ''):
    totalChance-=1
  else:
    for index in indexes:
      fill[index] = userInput
      checkWords[index] = ''
      correct+=1

clear()
print(f"Please find the word : {','.join(fill)}")

if(totalChance!= 0):
  print("You Are won")
else:
  print("You lost")

print('game over')
