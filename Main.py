import random
import time

while True:
    query = input("Do you want Coin Flip, Dice Roll or Spin? (Type coin, dice, or spin): ")
    Fl = query[0].lower()
    if query == '' or not Fl in ['c', 'd', 's']:
        print('Please answer with Dice, Coin, or Spinner!')
    else:
        break
if Fl == 'c':

    total_heads = 0
    total_tails: int = 0

    count_raw = input("Enter the number of times you want to Coin Flip: ")
    time.sleep(0.5)

    count = int(count_raw)
    z = count

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
    print("Giving you a probability of landing on heads was", (total_heads/z))
    time.sleep(0.6)

    print("You flipped tails", total_tails, "times ")
    print("Giving you a probability of", (total_tails/z))
    time.sleep(0.6)

    input("Press Enter when Finished: ")

elif Fl == 'd':

    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0

    count_raw = input("Enter the amount of times you want to Dice Roll: ")

    count = int(count_raw)

    f = count

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
    print("Giving you a probability of", (total_1 / f))

    time.sleep(0.3)
    print("You hit two", total_2, " times")
    print("Giving you a probability of", (total_2 / f))

    time.sleep(0.3)
    print("You hit three", total_3, " times")
    print("Giving you a probability of", (total_3 / f))

    time.sleep(0.3)
    print("You hit four", total_4, " times")
    print("Giving you a probability of", (total_4 / f))

    time.sleep(0.3)
    print("You hit five", total_5, " times")
    print("Giving you a probability of", (total_5 / f))

    time.sleep(0.3)
    print("You hit six", total_6, " times")
    print("Giving you a probability of", (total_6 / f))

    time.sleep(0.5)
    input("Press Enter when Finished: ")

elif Fl == 's':

    S_1 = 0
    S_2 = 0
    S_3 = 0
    S_4 = 0
    S_5 = 0
    S_6 = 0

    count_raw = input("Enter the amount of times you want to Spin: ")
    count = int(count_raw)
    p = count

    x = input("How many colors do you want? ")
    r = int(x)

    while count > 0:

        number = random.randint(1, r)

        if number == 1:
            print("1")
            S_1 += 1
            count -= 1

        if number == 2:
            print("2")
            S_2 += 1
            count -= 1

        if number == 3:
            print("3")
            S_3 += 1
            count -= 1

        if number == 4:
            print("4")
            S_4 += 1
            count -= 1

        if number == 5:
            print("5")
            S_5 += 1
            count -= 1

        if number == 6:
            print("6")
            S_6 += 1
            count -= 1
    time.sleep(0.3)
    if r:
        print("You hit Yellow", S_1, " times")
        print("Giving you a probability of", (S_1 / p))
        time.sleep(0.3)
    if r == 1 or 2:
        print("You hit Black", S_2, " times")
        print("Giving you a probability of", (S_2 / p))
        time.sleep(0.3)
    if r == 1 or 2 or 3:
        print("You hit Red", S_3, " times")
        print("Giving you a probability of", (S_3 / p))
        time.sleep(0.3)
    if r == 1 or 2 or 3 or 4:
        print("You hit Orange", S_4, " times")
        print("Giving you a probability of", (S_4 / p))
        time.sleep(0.3)
    if r == 1 or 2 or 3 or 4 or 5:
        print("You hit Blue", S_5, " times")
        print("Giving you a probability of", (S_5 / p))
        time.sleep(0.3)
    if r == 1 or 2 or 3 or 4 or 5 or 6:
        print("You hit Red", S_6, " times")
        print("Giving you a probability of", (S_6 / p))
        time.sleep(0.5)

    input("Press Enter when Finished: ")
