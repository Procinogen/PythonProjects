import math

def ReAskTwo():
    usrInput = raw_input("[P1] Rock, paper, or scissors? ")
    usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
    if usrInput.lower() == "rock":
        if usrInputTwo.lower() == "paper":
            print "[P1] loses and [P2] wins!"
        elif usrInputTwo.lower() == "scissors":
            print "[P2] wins and [P1] loses!"
        elif usrInputTwo.lower() == "rock":
            print "It's a tie!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    elif usrInput.lower() == "paper":
        if usrInputTwo.lower() == "paper":
            print "It's a tie!"
        elif usrInputTwo.lower() == "scissors":
            print "[P1] loses and [P2] wins!"
        elif usrInputTwo.lower() == "rock":
            print "[P1] wins and [P2] loses!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    elif usrInput.lower() == "scissors":
        if usrInputTwo.lower() == "paper":
            print "[P1] wins and [P2] loses!"
        elif usrInputTwo.lower() == "scissors":
            print "It's a tie!"
        elif usrInputTwo.lower() == "rock":
            print "[P2] loses and [P1] wins!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    return

def TwoP():
    usrInput = raw_input("[P1] Rock, paper, or scissors? ")
    usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
    if usrInput.lower() == "rock":
        if usrInputTwo.lower() == "paper":
            print "[P1] loses and [P2] wins!"
        elif usrInputTwo.lower() == "scissors":
            print "[P2] wins and [P1] loses!"
        elif usrInputTwo.lower() == "rock":
            print "It's a tie!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    elif usrInput.lower() == "paper":
        if usrInputTwo.lower() == "paper":
            print "It's a tie!"
        elif usrInputTwo.lower() == "scissors":
            print "[P1] loses and [P2] wins!"
        elif usrInputTwo.lower() == "rock":
            print "[P1] wins and [P2] loses!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    elif usrInput.lower() == "scissors":
        if usrInputTwo.lower() == "paper":
            print "[P1] wins and [P2] loses!"
        elif usrInputTwo.lower() == "scissors":
            print "It's a tie!"
        elif usrInputTwo.lower() == "rock":
            print "[P2] loses and [P1] wins!"
        else:
            "[P2] Not an option, try again"
            usrInputTwo = raw_input("[P2] Rock, paper, or scissors? ")
            ReAskTwo()
    else:
        print "[P1] Not an option, try again"
        TwoP()
    return
TwoP()
