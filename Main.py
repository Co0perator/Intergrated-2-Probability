import random
#import time

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
        
    #time.sleep(0.5)

    count = int(input("Enter the number of times you want to Coin Flip: "))
    z = count

    while count > 0:

        coin = random.randint(1, 2)

        if coin == 1:
            print("Heads!")
            total_heads += 1

        else:
            print("Tails!")
            total_tails += 1
        
        count -= 1

    #time.sleep(0.4)

    print("You flipped heads", total_heads, "times ")
    print("Giving you a probability of landing on heads was", (total_heads/z))
    #time.sleep(0.6)

    print("You flipped tails", total_tails, "times ")
    print("Giving you a probability of", (total_tails/z))
    #time.sleep(0.6)

elif Fl == 'd':

    total = [0 for i in range(6)]

    count = int(input("Enter the amount of times you want to Dice Roll: "))

    f = count

    while count > 0:

        number = random.randint(1, 6)

        print(number)
        total[number - 1] += 1
        count -= 1
    
    for i in range(6):
        #time.sleep(0.3)
        print("You hit side " + str(i), "[" + str(total[i]) +"]", "times")
        print("Giving you a probability of", (total[i] / f))

    #time.sleep(0.5)

elif Fl == 's':

    S = [0 for i in range(6)]
    
    count = int(input("Enter the amount of times you want to Spin: "))
    p = count
    
    r = int(input("How many colors do you want? (Out of 6)"))

    while count > 0:

        number = random.randint(1, r)

        print(number)
        S[number - 1] += 1
        count -= 1
        
    #time.sleep(0.3)
    if r:
        print("You hit Yellow", S[0], " times")
        print("Giving you a probability of", (S[0] / p))
        #time.sleep(0.3)
        
    if r in range(1,3):
        print("You hit Black", S[1], " times")
        print("Giving you a probability of", (S[1] / p))
        #time.sleep(0.3)
        
    if r in range(1,4):
        print("You hit Red", S[2], " times")
        print("Giving you a probability of", (S[2] / p))
        #time.sleep(0.3)
        
    if r in range(1,5):
        print("You hit Orange", S[3], " times")
        print("Giving you a probability of", (S[3] / p))
        #time.sleep(0.3)
        
    if r in range(1,6):
        print("You hit Blue", S[4], " times")
        print("Giving you a probability of", (S[4] / p))
        #time.sleep(0.3)
        
    if r in range(1,7):
        print("You hit Red", S[5], " times")
        print("Giving you a probability of", (S[5] / p))
        #time.sleep(0.5)

input("Press Enter when Finished: ")
