def llength(x1, x2, y1, y2):
	result = (int(x2) - int(x1))**2 + (int(y2) - int(y1))**2
	return result
	
cont = True
while cont == True:
	print(llength(input("x_1 = "), input("x_2 = "), input("y_1 = "), input("y_2 = ")))
	cont = bool(input("continue? "))