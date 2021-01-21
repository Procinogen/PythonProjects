def makes10(a, b):
	if a == 10 or b == 10:
		print "True"
	elif a + b == 10:
		print "True"
	else:
		print "False"
	return

x = raw_input("a = ")
y = raw_input("b = ")
makes10(int(x), int(y))
input()