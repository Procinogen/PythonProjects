def Start():
	print("Hello, traveller! Welcome to the world of Programmia! My name is Totoral. Pretend I gave you some kind of exposition,")
	ClassAsk()
	return
	
def ClassAsk():
	print("-----------------------------------")
	print("Alright, choose a class.")
	print(">NEET   Edgelord   Buisness Man ")
	choose = str(input("Which class do you want to be? (Type in the name of the class, caps don't count.) >"))
	if(choose.lower() == "neet"):
		print(">NEET    Edgelord    Buisness Man")
		Be = str(input("Is this the class you want to be? (Type yes or no) "))
		if (Be.lower() == "no"):
			ClassAsk()
		elif (Be.lower() == "yes"):
			print("-----------------------------------")
			print("Alrighty then")
		else:
			print("What?")
			ClassAsk()
	elif (choose.lower() == "edgelord"):
		print("NEET    >Edgelord    Buisness Man")
		Be = str(input("Is this the class you want to be? (Type yes or no) "))
		if (Be.lower() == "no"):
			ClassAsk()
		elif (Be.lower() == "yes"):
			print("-----------------------------------")
			print("Alrighty then")
		else:
			print("What?")
			ClassAsk()	
	elif (choose.lower() == "buisness man"):
		print("NEET    Edgelord    >Buisness Man")
		Be = str(input("Is this the class you want to be? (Type yes or no) "))
		if (Be.lower() == "no"):
			ClassAsk()
		elif (Be.lower() == "yes"):
			print("-----------------------------------")
			print("Alrighty then")
		else:
			print("What?")
			ClassAsk()
	else:
		print("That's not an option.")
		ClassAsk()
	return
Start()