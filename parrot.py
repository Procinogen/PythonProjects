''' We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. '''

t = raw_input("Is talking? True or False: ")
h = raw_input("Hour. 1-23: ")
def parrot_trouble(talking, hour):
	if (talking == True and hour < 7) or (talking == True and hour > 20):
		print "You're in trouble, boi."
	else:
		print "Ya did it."
	return

parrot_trouble(bool(t), int(h))
input()