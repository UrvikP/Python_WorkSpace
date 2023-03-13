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
print("Your mission is to find the treasure.")

choice = input(
    'You have arrived at Dragons Ridge. There are 2 paths you can take.\nWill you go left or right?')

if choice == 'left':
    second_choice = input('You went throught the shifting rifts, arriving at an bizzare island filled with towering trees and air so dense, it can be seen by the naked eye.'
                          '\n You notice there are giant imprints on the ground, creating a trail that leads further in the forest of giant Trees.'
                          '\n Will you follow the trail or observe the surroundings?')
    if second_choice == 'observe':
        final_choice = input('You chose to observe the surrounds, when suddenly deep in the forest, you hear a mighty ROOOAAR.'
                             '\nThe sound vibrates throughtout the entire forrest, the trees tremble, the ground quakes'
                             '\nAnimals of all shapes and sizes scurrying about in chaos.'
                             '\nWhat will you do, og towards the sound, or run away')
