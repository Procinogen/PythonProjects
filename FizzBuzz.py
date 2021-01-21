''' Write a program that prints the numbers from 1 to 100.
But for multiples of three print Fizz instead of the number, and for the multiples of five print Buzz.
For numbers which are multiples of three and five print FizzBuzz '''

def PrintNum():
	for x in range(1, 101):
		if x % 5 == 0 and x % 3 == 0:
			print "FizzBuzz " + str(x)
		elif x % 3 == 0:
			print "Fizz " + str(x)
		elif x % 5 == 0:
			print "Buzz " + str(x)
		else:
			print x
	return
	
PrintNum()
input()