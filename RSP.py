import time
import random
import os
def rsp():
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
def df():
    print("╔══╗╔═══╦╗──╔╗───  ╔═══╦═══╗  ╔═══╦═══╦════╦═══╗")
    time.sleep(0.2)
    print("║╔╗║║╔═╗║║──║║───  ║╔═╗║╔══╝  ║╔══╣╔═╗║╔╗╔╗║╔══╝")
    time.sleep(0.2)
    print("║╚╝╚╣║─║║║──║║───  ║║─║║╚══╗  ║╚══╣║─║╠╝║║╚╣╚══╗")
    time.sleep(0.2)
    print("║╔═╗║╚═╝║║─╔╣║─╔╗  ║║─║║╔══╝  ║╔══╣╚═╝║─║║─║╔══╝")
    time.sleep(0.2)
    print("║╚═╝║╔═╗║╚═╝║╚═╝║  ║╚═╝║║───  ║║──║╔═╗║─║║─║╚══╗")
    time.sleep(0.2)
    print("╚═══╩╝─╚╩═══╩═══╝  ╚═══╩╝───  ╚╝──╚╝─╚╝─╚╝─╚═══╝")
    time.sleep(0.5)
    qu = input("Enter your question: ")
    time.sleep(0.8)
    os.system('clear')
    ba = random.randint(1, 8)
    if ba == 1:
        print("Yes")
    elif ba == 2:
        print("No")
    elif ba == 3:
        print("Maybe")
    elif ba == 4:
        print("Is Unknown")
    elif ba == 5:
        print("Star Server Overloaded, Ask Later")
    elif ba == 6:
        print("I'll Make You Sad Or Happy. The Answer Is No")
    elif ba == 7:
        print("The Stars Say No, But I Don't Believe Them")
    else:
        print("The Stars Ignored You...")
def hr():
    print("╔╗─╔╗───────────╔═══╗")
df()
def cls():
    os.system('clear' if os.name=='nt' else 'cls')

# now, to clear the screen
cls()