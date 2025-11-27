print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
game_over = (r'''
    █████▀█████████████████████
    █─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█
    █─██▄─██─▀─███─█▄█─███─▄█▀█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀
    ████████████████████████
    █─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
    █─██─██▄▀▄███─▄█▀██─▄─▄█
    ▀▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at the crossroads trying to find the way to the treasure. \n"
                  "Where should you go? Press L for left and R for right.")
if direction == "L":
    print("You continue on your path without any trouble.")
    print()
elif direction == "R":
    print("You fall into a hole. Be cautious next time! \nGame over.")
    print(game_over)
    exit()
else:
    print("What the hell are you doing? You can't just put in random stuff and expect to bypass! \n"
          "Game over.")
    print(game_over)
    exit()

swim = input("You have arrived at the river with no bridge in sight. \n"
             "You can cross the river by swimming or wait until the river can be passed by foot. \n"
             "Do you swim or wait? Press S for swim and W for wait.")
if swim == "S":
    print("You are attacked by a trout and this trout is not playing around. \nGame over.")
    print(game_over)
    exit()
elif swim == "W":
    print("And this was the right call! You crossed the river with no casualties and you are on the way to the treasure!")
    print()
else:
    print("You. Shall. Not. Pass! \nGAME OVER.")
    print(game_over)
    exit()

door = input("Now you've finally arrived to the castle where it is believed the treasure can be found. \n"
             "You can see three doors, and all these doors differ in color. \n"
             "Which door do you choose to enter? Type R for red, B for blue and Y for yellow.")
if door == "R":
    print("Congratulations, you got burned by the flames of Avernus and got turned into the finest steak! \nGame over.")
    print(game_over)
    exit()
elif door == "B":
    print("Congratulations, you got eaten by the beasts of unknown origin! \nGame over.")
    print(game_over)
    exit()
elif door == "Y":
    print("You found the treasure and the respect of your community as a nice bonus! \n"
          "You win!")
else:
    print("Game over is a suitable punishment for those who refuse to listen to the instructions. \nGAME. OVER.")
    print(game_over)
    exit()