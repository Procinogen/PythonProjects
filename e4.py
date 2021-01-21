def DivisorFind():
    usrInput = int(raw_input("Enter a number to find all of it\'s divisors. "))
    rnge = range(2, usrInput)
    divisors = []
    
    for elem in rnge:
        if usrInput % elem == 0:
            divisors.append(elem)

    print divisors

    GoAgain = raw_input("Want to do that again? (Yes or No)")
    if GoAgain == "Yes" or GoAgain == "yes":
        DivisorFind()
    else:
       print "Stopping..."
       
    return

DivisorFind()
