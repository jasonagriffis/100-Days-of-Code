# A simple text-based choose your own adventure.
# Jason Griffis
# 9/8/2022

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("As you walk along the shoreline, you come to a path diverging in two directions.\n")
answer = input("Do you go left or right? (L or R) ")

if answer.lower() == "l":
  print("\nYou come upon a large lake, it might be possible to swim across.\n")
  print("However, you spy a ferryman off in the distance rowing toward you.\n")
  answer = input("Do you want to swim or wait for the ferry? (S or W) ")
  if answer.lower() == "w":
    print("\nAfter crossing the lake on the ferry, you came to a castle and entered the courtyard.\n")
    print("The massive front wall of the castle has only three openings to enter into the castle beyond.\n")
    print("You have to decide between opening a blue, red, or yellow door.\n")
    answer = input("Which do you choose; blue, red, or yellow? (B, R, or Y) ")
    if answer.lower() == "b":
      print("Snarling, hungry beasts lunge and attack you. Knocking you unconcious on the floor and devouring your flesh.\n")
      print("Game Over!")
    elif answer.lower() == "r":
      print("A burst of flame shoots forth, incinerating your body and belongings.\n Game Over!")
    elif answer.lower()== "y":
      print("\nThe door opens onto a short corridor. On the far end you find an unguarded room and stealthily slide in.\n")
      print("In the room you find a very large chest, filled to overflowing with treasure!!\n")
      print("You've found the treasure and mastered the island! Congratulations!")
    else:
      print("You decide to forego any further adventures, and return home empty handed.\n Game Over.")
  else:
    print("As you attempt to cross the lake alone, a humongous trout swallows you whole!\n Game Over!")
else:
  print("\nYou fall into a deep hole that is riddled with sharpened stakes, and die. Game Over!")
