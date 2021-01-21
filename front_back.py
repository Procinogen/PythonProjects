def front_back(string):
	x = string
	a = x[-1]
	b = x[:1]
	x = x[:-1]
	x = x[1:]
	x = a + x
	x = x + b
	print x
	return
	
front_back("swag")
input()