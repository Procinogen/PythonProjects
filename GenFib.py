""""
def FibGen(Length):
	rnge = range(1, Length)
	Fibs = []
	for elem in rnge:
		if elem == 0 or elem == 1 or elem == 2:
			Fibs.append(1)
		else:
			Fibs.append(Fibs[Elem] + Fibs[Elem-1])
	return Fibs

def GetFibs():
	UsrInput = int(raw_input("How many Fibonacci numbers do you want to generate? "))
	Ans = FibGen(UsrInput)
	print Ans
	return
	
GetFibs()
raw_input("")
"""

def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()