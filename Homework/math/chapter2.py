def distance(x1, y1, x2, y2):
	return ((float(x2) - float(x1))**2) + (float(y2) - float(y1))**2

def midseg(x1, y1, x2, y2):
	return ((float(x1) + float(x2)) / 2, (float(y1) + float(y2)) / 2)

def radius(x1, y1, x2, y2):
	return ((float(x2) - float(x1))**2) + (float(y2) - float(y1))**2

def slope(x1, y1, x2, y2):
	dx = (float(y2) - float(y1))
	dy =(float(x2) - float(x1))
	return str(dx) + " / " + str(dy)

def main():
	cont = True
	while cont == True:
		option = int(input("Which function? 1 = distance; 2 = mid segments; 3 = radius; 4 = slope; 0 = stop program: "))
		if option == 0:
			print("Program ending")
			cont = False
		elif option == 1:
			print(str("d = √") + str(distance(input("x_1 = "), input("y_1 = "), input("x_2 = "), input("y_2 = "))))
		elif option == 2:
			print(str("M_xy = ") + str(midseg(input("x_1 = "), input("y_1 = "), input("x_2 = "), input("y_2 = "))))
		elif option == 3:
			print(str("r^2 =") + str(distance(input("x_1 = "), input("y_1 = "), input("x_2 = "), input("y_2 = "))))
		elif option == 4:
			print(str("m = ") + str(slope(input("x_1 = "), input("y_1 = "), input("x_2 = "), input("y_2 = "))))
	return
	
main()