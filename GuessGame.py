import random
numGuess = random.randint(1, 9)
i = 0
def GuessGame():
    GuessedNum = raw_input("Guess a number from 1 to 9! ")
    global i
    i += 1
    print i
    if GuessedNum == "exit":
        print "Guess attempts: " + str(i)
        print "Number: " + str(numGuess)
    elif int(GuessedNum) > numGuess:
        print "Too high!"
        GuessGame()
    elif int(GuessedNum) < numGuess:
        print "Too low!"
        GuessGame()
    elif int(GuessedNum) == numGuess:
        print "Congrats! You did it!"
        print "Guess attempts: " + str(i)
        print "Number: " + str(i)
    else:
        print "error?"
    return

GuessGame()
