import random

def AskUser():
	print("Select the strength of the password you want to generate")
 	PassStrength = str(raw_input("Weak, medium, or strong? "))
	return PassStrength
	
def GenPass():
	Ps = AskUser()
	if "weak" in Ps.lower():
		weakPasswords = ["password", "12345", "qwerty", "dragon", "soccer", "love"]
		print "Here's your randomly generated password: '" + weakPasswords[random.randint(0, 5)] + "'"
	elif "medium" in Ps.lower:
		print "lol"
	return
	
GenPass()
input("Press enter to exit program")