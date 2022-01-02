import random

def intToStr(array):
  strs = [ str(value) for value in array ]
  print(strs)
  return strs

def askChanges():
  return int(input(print("could you switch 1 or 11?")))

def playCard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user = random.choices(cards,  k=2)
  computer = [random.choice(cards)]
  print("Player Card is ", ','.join(intToStr(user)))
  print("Computer Card is ", ','.join(intToStr(computer)))
  confirm = input(print("You need to take another card? yes or no"))

  if(confirm.lower() == 'yes'):
    user.append(random.choice(cards))
    print("Your Card is ", ','.join(intToStr(user)))

  changes = False
  for i in range(0, len(user)):
    have = user[i]
    if(have == 11):
      changes = True
      user[i] = askChanges()

  if(changes == True):
    print("Final changes of Player Card is ", ','.join(intToStr(computer)))

  computer.append(random.choice(cards))
  print("Computer Card is ", ','.join(intToStr(computer)))

  changes = False
  computerTotal = sum(computer)
  if(computerTotal > 21):
    computer[1] = 1
    changes=True
  if(changes==True):
    print("Final changes of Computer Card is ", ','.join(intToStr(computer)))

  computerTotal = sum(computer)
  userTotal = sum(user)

  if(userTotal == computerTotal):
    print("Match is draw")
  elif(userTotal > computerTotal):
    print("Play won")
  else:
    print("computer won")

  rematch = input(print("Rematch yes or no"))
  if(rematch == 'yes'):
    playCard()
  else:
    print("game over")

playCard()
