string = str(raw_input("Type in anything, I\'ll see if it\'s a palindrome! "))
ArrOne = []
ArrTwo = []

NumberOfTimes = string

for i in NumberOfTimes:
    ArrOne.append(i)
    ArrTwo.append(i)

ArrOne.reverse()

if ArrOne == ArrTwo:
    print "\'" + string + "\' is a palindrome!"
else:
    print "\'"+ string + "\' is not a palindrome!"
