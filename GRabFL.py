import random
a = random.sample(xrange(20), 10)
print "First List: " + str(a)
def GrabFL():
	Last = len(a)
	b = []
	b.append(a[0])
	b.append(a[-1])
	print "First and last elements of first list: " + str(b)
	return
	
GrabFL()
raw_input("")
