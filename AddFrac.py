import math
import time
def AddFrac():
    num1 = int(raw_input("Numerator 1: "))
    den1 = int(raw_input("Denominator 1: "))
    num2 = int(raw_input("Numerator 2: "))
    den2 = int(raw_input("Denominator 2: "))

	
    ComDen = den1 * den2
    NumFrac1 = num1 * den2
    NumFrac2 = num2 * den1

    ans = NumFrac1 + NumFrac2
    i = 0
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    i = 0
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    i = 0
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    if ans == 1 and ComDen == 1:
        print 1
    else:
        print str(ans) + "/" + str(ComDen)
		
	Ask()
    return

def SubFrac():
    num1 = int(raw_input("Numerator 1: "))
    den1 = int(raw_input("Denominator 1: "))
    num2 = int(raw_input("Numerator 2: "))
    den2 = int(raw_input("Denominator 2: "))

    ComDen = den1 * den2
    NumFrac1 = num1 * den2
    NumFrac2 = num2 * den1

    ans = NumFrac1 - NumFrac2
    i = 0
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    i = 0
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    i = 05
    while i < ComDen:
        i += 1
        if ans % i == 0 and ComDen % i == 0:
            ans /= i
            ComDen /= i
    if ans == 1 and ComDen == 1:
        print 1
    else:
        print str(ans) + "/" + str(ComDen)
	
	Ask()
    return

def MultFrac():
    num1 = int(raw_input("Numerator 1: "))
    den1 = int(raw_input("Denominator 1: "))
    num2 = int(raw_input("Numerator 2: "))
    den2 = int(raw_input("Denominator 2: "))

    ComDen = den1 * den2
    ans = num1 * num2
    i = 0
		
    if ans == 1 and ComDen == 1:
        print 1
    else:
        print str(ans) + "/" + str(ComDen)
	
	Ask()
    return	

def Ask():
	usrInpt = raw_input("What would you like to do? ")
	if "add" in usrInpt.lower():
		AddFrac()
	elif "subtract" in usrInpt.lower():
		SubFrac()
	elif "multiply" in usrInpt.lower():
		MultFrac()
	elif "stop" in usrInpt.lower() or "exit" in usrInpt.lower():
		print "Okay, see you again!"
		time.sleep(2)
	else:
		print "Oh, that doesn't seem to be an option."
		Ask()
	return

Ask()
