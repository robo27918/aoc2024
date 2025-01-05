import random
import time
position = 16
win_tile = 32
have_star = False
have_foot = False
turns = 0
money = 100

def shop(money, have_foot, have_star):
  print("Oh! You landed at the store! Do you want to buy something?")
  want_to_buy = input("Type Y for Yes, anything else for no:")
  if want_to_buy.lower() == "y":
    print("You have", money, "coins.")
    if money >= 50:
      print("You can buy one of these:")
      print("Super Star (30 coins) - can be used at any time to add 5 to your roll.")
      print("Cyborg Foot (50 coins) - can be used at any time to double your roll.")
      print("What do you want to buy?")
      product_choice = input("Type 1 for Superstar, 2 for Cyborg foot, and anything else for no thanks:")
      if product_choice == "1":
        print("You bought the Superstar! You can use it any time.")
        have_star = True
        money = money - 30
        print("You have", money, "coins.")
      elif product_choice == "2":
        print("You bought the Cyborg foot! You can use it any time.")
        have_foot = True
        money = money - 50
        print("You have", money, "coins.")
      else:
        print("Well, your loss!")
    elif money >= 30:
      print("You can buy one of these:")
      print("Super Star (30 coins) - can be used at any time to add 5 to your roll.")
      print("What do you want to buy?")
      product_choice = input("Type 1 for Superstar and anything else for no thanks:")
      if product_choice == "1":
        print("You bought the Superstar! You can use it any time.")
        have_star = True
        money = money - 30
        print("You have", money, "coins.")
      else:
        print("Well, your loss!")
    else:
      print("Sorry, you don't have enough money for anything.")
  else:
    print("Well, your loss!")
  return money, have_foot, have_star
  
def welcome():  
  print("Welcome player to \"The Board Game That Makes You Want To Throw Your Computer Out The Window 2.0!\" ")
  time.sleep(3)
  print("Yes that is the name of the board game. Don't laugh. Your going to regret it.")
  time.sleep(3)
  print("Anyways, there are 32 squares in this board game, some good some bad.")
  time.sleep(3)
  print("and the end will be square 32! Go ahead play as many times as you like, see how many turns it take you!")
  time.sleep(3)
  print()

def moreMoney(money, addmoney,):
  money = money + addmoney
  print("You landed on a money square! You now have", money, "coins.")
  return money

welcome()
print("Your position is at square 1.")
while position < win_tile:
  turns = turns + 1
  dice_roll =0#YY random.randint(1,3)
  print("Your roll is", dice_roll,"!")
  if have_foot or have_star:
    if have_foot:
      print("You have a Cyborg Foot (dicerole*2), do you want to use it?")
      print("Enter Y for yes, anything else for no.")
      if input("Enter your choice:").lower() == "y":
        print("You doubled your roll!")
        position = position + dice_roll*2
        have_foot = False
      else:
        position = position + dice_roll
    if have_star:
      print("You have a Superstar (dicerole+5), do you want to use it?")
      print("Enter Y for yes, anything else for no.")
      if input("Enter your choice:").lower() == "y":
        print("You added 5 to your roll!")
        position = position + dice_roll + 5
        have_star = False
      else:
        position = position + dice_roll
  else:  
    position = position + dice_roll
  if position > 32:
    position = 32
  print("Your position is at square", position, ".")
  #Money
  if position == 3:
    money = moreMoney(money, 20)
  if position == 5 or position == 8:
    money = moreMoney(money, 10)
  if position == 10:
    money = moreMoney(money, 5)
  if position == 13:
    money = moreMoney(money, 25)
  #Skips
  if position == 12:
    position = 7
    print("Oh no! You fell of square 12 to square 7!")
  if position == 19:
    position = 23
    print("Yay! You found a shortcut to square 23!")
  if position == 29:
    position = 1
    print("Oh no! You fell of square 29 to square 1!")
  #Random Teleport
  if position == 27:
    position = random.randint(1,32)
    print("You got randomly teleported to square", position, "!")
  #Jail
  if position == 22:
    jail_time = random.randint(30,120)
    print("Oops! You landed in Jail! You have to wait for", jail_time, "seconds.")
    time.sleep(jail_time)
  '''
    TODO: Implement the user using the product and update the boolean variables
  '''
  #Shop
  if position == 16:
    money, have_foot,have_star = shop(money, have_foot, have_star)
#End Stuff
  input("Please press enter to continue.")
  print()
print("Congratulations! You won!")
time.sleep(2)
print("You took", turns,"turns to reach the end!")