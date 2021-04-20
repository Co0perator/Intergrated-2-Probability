import random
import time

while True:
    query = input("Do you want 40 Coin Flips or 50 Dice Rolls? (Type coin or dice): ")
    Fl = query[0].lower()
    if query == '' or not Fl in ['c', 'd']:
        print('Please answer with Dice or Coin!')
    else:
        break
if Fl == 'c':

    total_heads = 0
    total_tails = 0
    count = 40

    while count > 0:

        coin = random.randint(1, 2)

        if coin == 1:
            print("Heads!")
            total_heads += 1
            count -= 1

        elif coin == 2:
            print("Tails!")
            total_tails += 1
            count -= 1

    time.sleep(0.4)
    print("You flipped heads", total_heads, "times ")
    time.sleep(0.4)
    print("You flipped tails", total_tails, "times ")

    time.sleep(0.4)
    input("Press Enter when Finished: ")

elif Fl == 'd':

    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0
    count = 50

    while count > 0:

        number = random.randint(1, 6)

        if number == 1:
            print("1")
            total_1 += 1
            count -= 1

        if number == 2:
            print("2")
            total_2 += 1
            count -= 1

        if number == 3:
            print("3")
            total_3 += 1
            count -= 1

        if number == 4:
            print("4")
            total_4 += 1
            count -= 1

        if number == 5:
            print("5")
            total_5 += 1
            count -= 1

        if number == 6:
            print("6")
            total_6 += 1
            count -= 1

    time.sleep(0.3)
    print("You hit one", total_1, " times")
    time.sleep(0.3)
    print("You hit two", total_2, " times")
    time.sleep(0.3)
    print("You hit three", total_3, " times")
    time.sleep(0.3)
    print("You hit four", total_4, " times")
    time.sleep(0.3)
    print("You hit five", total_5, " times")
    time.sleep(0.3)
    print("You hit six", total_6, " times")

time.sleep(0.5)
input("Press Enter when Finished: ")
