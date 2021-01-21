def AskString():
	TheString = raw_input("Give me a sentence, I'll reverse it. ")
	return TheString
	
def Reverse():
	ToReverse = AskString().split(" ")
	ReversedTxt = ToReverse[::-1]
	print " ".join(ReversedTxt)
	return
	
Reverse()
input(" ")
