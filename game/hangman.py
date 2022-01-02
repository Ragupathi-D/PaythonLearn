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
print(checkWords)
while(leterLength != correct and totalChance != 0):
  clear()
  print(f"Please find the word, {','.join(fill)}")
  print(f"Your total chance is {totalChance}")
  userInput = input('Please enter the word : ').lower()
  check = userInput in checkWords
  if(not check or userInput != ''):
    totalChance-=1
  else:
    index = checkWords.index(userInput)
    print('index', index)
    fill[index] = userInput
    checkWords[index] = ''
    correct+=1;

clear()
print(f"Please find the word, {','.join(fill)}")

if(totalChance!= 0):
  print("You Are won")
else:
  print("You lost")

print('game over')
