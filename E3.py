a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessThanFive = []
greaterThanTen = []
evenNumbers = []

for foo in a:
    if foo < 5:
        lessThanFive.append(foo)
        if (foo % 2) == 0:
                evenNumbers.append(foo)
    elif foo > 5:
        greaterThanTen.append(foo)
        if (foo % 2) == 0:
                evenNumbers.append(foo)
print "Numbers less than five: " + str(lessThanFive)
print "Numbers greater than are greater than ten: " + str(greaterThanTen)
print "Numbers that are even: " + str(evenNumbers)

