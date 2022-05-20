#import
import random

#init

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False
won = False

dist = 0
thirst = 0
tired = 0

#readHS
score = open("Highscores.txt", "r")
scores = score.read()
print(scores)
score.close()
#//#

z = 0

natives = -20

drinks = 3

while done == False:
    print("--------------------")
    print("[a] Drink from your canteen.")
    print("[b] Ahead moderate speed.")
    print("[c] Ahead full speed.")
    print("[d] Stop for the night.")
    print("[e] Status check.")
    print("[q] Quit.")
    print("--------------------")

    #randoms
    event = random.randint(0,100)
    if event == 0:
        print("YOU FOUND AN OASIS")
        print("Drinks, thirst, tiredness all replenished and the natives temporarily lost sight of you.")
        drinks = 3
        thirst = 0
        tired = 0
        natives = natives - 10
    if event == 1:
        print("--------------------")
        print("A line.")
        print("--------------------")
    if event == 2:
        print("The world has ended.")
        print("Funnily enough, you are dead.")
        done = True
    if event == 3:
        print("A slarlac caught you.")
        print("Unlike RT-6734, you are dead.")
        done = True
    if event == 4:
        print("A turtle you do see, crawling across though desert.")
    if event == 5:
        print("The camel does a poopy")
        print("You died.")
        done = True
    if event == 6:
        print("The natives had a big gun.")
        print("They died")
        won = True
        done = True
    if event == 7:
        print("You saw a helicopter and shot a flare.")
        print("They saw you.")
        print("But couldn't give a flying purple monkeys.")
        print("What an L")
        natives = natives + 5
    if event == 8:
        print("You found treasure!")
        z = z - 2
    if event == 9:
        print("C'thulu came down from the heavens.")
        print("He gave you a blue rock.")
        z = z - 1
    if event == 10:
        print("Milk.")
    
    #death
    if thirst > 6:
        print("You died of thirst.")
        done = True
    elif thirst > 4:
        print("You're thirsty.")

    if tired > 8:
        print("You got too exausted and dieded.")
        done = True
    elif tired > 5:
        print("You're tired.")

    if natives > -1:
        print("The natives caught up and dismembered you.")
        done = True
    elif natives > -15:
        print("The natives are close.")
    
    if done == False:
        if dist > 199:
            print("You won")
            done = True
            won = True

    #inputs
    if done == False:
        choice = input(" ")

        if choice.lower() == "q":
            done = True
        elif choice.lower() == "e":
            dist = str(dist)
            drinks = str(drinks)
            natives = str(natives)
            print("Miles travelled: " + dist)
            print("Drinks in canteen: " + drinks)
            print("The natives are " + natives + " miles.")
            dist = int(dist)
            drinks = int(drinks)
            natives = int(natives)
        elif choice.lower() == "d":
            tired = 0
            natives = natives + random.randint(7,14)
            print("The camel is happy!")
        elif choice.lower() == "c":
            thirst = thirst + 1
            tired = tired + random.randint(1,3)
            inc = random.randint(10,20)
            dist = dist + inc
            inc = str(inc)
            print("You travelled " + inc + " miles.")
            inc = int(inc)
            natives = natives + random.randint(7,14) - inc
        elif choice.lower() == "b":
            thirst = thirst + 1
            tired = tired + 1
            inc = random.randint(5,12)
            dist = dist + inc
            inc = str(inc)
            print("You travelled " + inc + " miles.")
            inc = int(inc)
            natives = natives + random.randint(7,14) - inc
        elif choice.lower() == "a":
            if drinks > 0:
                drinks = drinks - 1
                thirst = 0
                print("You feel refreshed")
            else:
                print("You have no drinks...")

        z = z + 1
        

if won == True:
    z = str(z)
    name = input("You got 200 miles in " + z + " turns. Enter your name: ")

    #writeHS    
    score = open("Highscores.txt", "a")
    score.writelines("\n" + name.upper() + ": " + z)
    score.close()
    #//#

    z = int(z)
