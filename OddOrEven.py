def ModeOne():
    print "Put in  a number, I\'ll say if it's odd, or even!"
    Input = int(raw_input(""))
    
    if Input % 2 == 0 and Input % 4 == 0:
        print 'Your number is a multiple of four! (It\'s also even)'  
    elif Input % 2 == 0:
        print 'Your number is even!'
    elif Input % 2 != 0:
        print 'Your number is odd!'  
    return

def ModeTwo():
    print "Put in  two numbers, If the second number divides evenly in to the first one, I'll tell you."
    num = int(raw_input('First number: '))
    check = int(raw_input('Second number: '))
    if num % check == 0:
        print 'It divides evenly!'
    else:
        print "It doesn\'t divde evenly!"
    return

def ModePick():
    WhichMode = raw_input("Mode One, or Mode Two? ")
    if WhichMode == "Mode One":
        ModeOne()
    elif WhichMode == "Mode Two":
        ModeTwo()
    else:
        print("That isn't a mode! Select again")
        ModePick()
    return

ModePick()
