print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************ascii.co.uk/art/treasure''')

print("welcome to treasure island.")

print("your mission is to find the treasure.")

if 0:
    # with exit()
    print("game line 1: you\'re at a crossroad. where do you want to go?")

    q1 = input("left or right?\n>> ").lower()
    if q1 == "right":
        print("Game over!")
        exit()

    print("game line 2")
    q2 = input("swim or wait?\n>> ")
    if q2 == "swim":
        print("Game over!")
        exit()

    print("game line 3")
    q3 = input("which door? red, blue yellow\n>> ")
    if q3 != "yellow":
        print("Game over!")
        exit()

    print("You Win!")

if 0:
    # with nested if statements
    q1 = input("left or right?\n>> ").lower()
    if q1 == "right":
        print("Game over!")

    else:
        print("game line 2")
        q2 = input("swim or wait?\n>> ")
        if q2 == "swim":
            print("Game over!")

        else:
            print("game line 3")
            q3 = input("which door? red, blue yellow\n>> ")
            if q3 != "yellow":
                print("Game over!")
            else:
                print("You Win!")


            
print("game line 1: you\'re at a crossroad. where do you want to go?")

q1 = input("left or right?\n>> ").lower()
if q1 == "left":
    print("game line 2")
    q2 = input("swim or wait?\n>> ")
    if q2 == "wait":
        print("game line 3")
        q3 = input("which door? red, blue yellow\n>> ")
        if q3 == "yellow":
            print("You Win!")
            print("You found the treasure")
        else:
            print("Game over!")
            exit()
    else:
        print("Game over!")
        exit()
else:
    print("Game over!")
    exit()
