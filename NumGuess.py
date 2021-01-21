def Ask():
    x = float(input("Pick a number ranging from 1-1000000. I'll try to guess to it. "))
    Check(x)
    return

def Check(ans):
    minnum = 0
    maxnum = 1000000
    x = ans
    y = 0
    guesses = 0
    while (y != x):
        print ("Minnum:" + str(minnum))
        print ("Maxnum:" + str(maxnum))
        print ("I guess " + str(y) + ".")
        print("--------------")
        y = (minnum + maxnum) / 2
        if (y > x):
            maxnum = y
        elif (y < x):
            minnum = y
        guesses += 1
    print ("-+=-FINAL ANSWER=+-")
    print ("Minnum:" + str(minnum))
    print ("Maxnum:" + str(maxnum))
    print ("The answer should be " + str(y) + ".")
    if (guesses == 1):  
        print ("The answer was found in " + str(guesses) + " guess.")
    else:
        print ("The answer was found in " + str(guesses) + " guesses.")
    return
Ask()
