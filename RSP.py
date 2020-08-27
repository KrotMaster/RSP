import time
import random
ft = 0
print("╔═══╗╔═══╗╔═══╗╔╗╔═╗")
print("║╔═╗║║╔═╗║║╔═╗║║║║╔╝")
print("║╚═╝║║║─║║║║─╚╝║╚╝╝")
print("║╔╗╔╝║║─║║║║_╔╗║╔╗║")
print("║║║╚╗║╚═╝║║╚═╝║║║║╚╗")
print("╚╝╚═╝╚═══╝╚═══╝╚╝╚═╝")
print(" ")
time.sleep(1)
print("╔═══╗╔═══╗╔══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗")
print("║╔═╗║║╔═╗║╚╣─╝║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║")
print("║╚══╗║║─╚╝─║║─║╚══╗║╚══╗║║─║║║╚═╝║║╚══╗")
print("╚══╗║║║─╔╗─║║─╚══╗║╚══╗║║║─║║║╔╗╔╝╚══╗║")
print("║╚═╝║║╚═╝║╔╣─╗║╚═╝║║╚═╝║║╚═╝║║║║╚╗║╚═╝║")
print("╚═══╝╚═══╝╚══╝╚═══╝╚═══╝╚═══╝╚╝╚═╝╚═══╝")
print(" ")
time.sleep(1)
print("╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗")
print("║╔═╗║║╔═╗║║╔═╗║║╔══╝║╔═╗║")
print("║╚═╝║║║─║║║╚═╝║║╚══╗║╚═╝║")
print("║╔══╝║╚═╝║║╔══╝║╔══╝║╔╗╔╝")
print("║║───║╔═╗║║║───║╚══╗║║║╚╗")
print("╚╝───╚╝─╚╝╚╝───╚═══╝╚╝╚═╝")
print(" ")
time.sleep(1)
print("How Many Times Do You Want To Play?")
time.sleep(1)
hmt = int(input("Write Here: "))
while ft < hmt:
    time.sleep(1)
    print(" ")
    print("It`s RSP The Game")
    if ft == 0:
        time.sleep(1)
    print("1. Rock")
    if ft == 0:
        time.sleep(1)
    print("2. Scissors")
    if ft == 0:
        time.sleep(1)
    print("3. Paper")
    if ft == 0:
        time.sleep(1)
    pl = int(input("Choose: "))
    if pl == 1:
        print(" ")
        print("You Are Choose a Rock")
        time.sleep(1)
        bot = random.randint(1, 3)
        if bot == 1:
            print("Your Opponent Choose a Rock")
            time.sleep(1)
            print("Draw")
            ft += 1
        elif bot == 2:
            print("Your Opponent Choose a Scissors")
            time.sleep(1)
            print("Victory")
            ft += 1
        else:
            print("Your Opponent Choose a Paper")
            time.sleep(1)
            print("Defeat")
            ft += 1
    elif pl == 2:
        print(" ")
        print("You Are Choose a Scissors")
        time.sleep(1)
        bot = random.randint(1, 3)
        if bot == 1:
            print("Your Opponent Choose a Rock")
            time.sleep(1)
            print("Defeat")
            ft += 1
        elif bot == 2:
            print("Your Opponent Choose a Scissors")
            time.sleep(1)
            print("Draw")
            ft += 1
        else:
            print("Your Opponent Choose a Paper")
            time.sleep(1)
            print("Victory")
            ft += 1
    else:
        print(" ")
        print("You Are Choose a Paper")
        time.sleep(1)
        bot = random.randint(1, 3)
        if bot == 1:
            print("Your Opponent Choose a Rock")
            time.sleep(1)
            print("Victory")
            ft += 1
        elif bot == 2:
            print("Your Opponent Choose a Scissors")
            time.sleep(1)
            print("Defeat")
            ft += 1
        else:
            print("Your Opponent Choose a Paper")
            time.sleep(1)
            print("Draw")
            ft += 1
