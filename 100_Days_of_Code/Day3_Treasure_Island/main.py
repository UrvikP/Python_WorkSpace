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
    'You have arrived at Dragons Ridge. There are 2 paths you can take.\nWill you go "left" or "right"?')

if choice == 'left':
    second_choice = input('You went throught the shifting rifts, arriving at a bizzare island filled with towering trees and air so dense, it can be seen by the naked eye.'
                          '\n You notice there are giant imprints on the ground, creating a trail that leads further in the forest of giant Trees.'
                          '\n Will you "follow" the trail or "observe" the surroundings?')
    if second_choice == 'observe':
        final_choice = input('You chose to observe the surrounds, when suddenly deep in the forest, you hear a mighty ROOOAAR.'
                             '\nThe sound vibrates throughtout the entire forrest, the trees tremble, the ground quakes'
                             '\nAnimals of all shapes and sizes scurrying about in chaos.'
                             '\nWhat will you do, go towards the sound (enter g), or run away (enter r)')
        if final_choice == 'r':
            print('You chose to flee, abondoning the quest for treasure. As you are running, You see a massive red creature soaring to the sky.'
                  '\nIt\'s a dragon!! Congratulations You lived to tell the tale.')
        else:
            print("You chose to  run toward the sound of the roar. As you are running, you feel a sudden sense of dread."
                  "\nAs you approach the center of the forest, you freeze in place, cold sweat dripping down."
                  "\nA colossal red dragon is staring right at you. It opens it's mouth and unleashes dragon fire."
                  "\nYou've died")
    else:
        print("You followed the trail. You hear a loud roar. Suddenly, everything darkens.\n You've died.")
else:
    print('You went through the right path, leading to rift that leads to endless void. You have died.')
