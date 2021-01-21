def CheckPrime():
	UsrInpt = int(raw_input("Choose a number, I'll check if it's prime. "))
	rnge = range(2, UsrInpt)
	isPrime = False
	for elem in rnge:
		if UsrInpt % elem == 0:
			print "This number is not a prime number!"
			isPrime = False
			break
		else:
			isPrime = True
	if isPrime == True:
		print "This number is prime!"
			
	CheckPrime()
	return
	
CheckPrime()