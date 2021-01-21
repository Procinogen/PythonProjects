import random
DaRange = xrange(1, 11)
List = []
for elem in DaRange:
	List.append(random.randint(1, 5))
def SortLst():
	rnge = xrange(0, max(List)+1)
	SortedList = []
	for elem in rnge:
		if elem in List:
			SortedList.append(elem)
	return SortedList

print List	
print SortLst()
raw_input("Press enter to end program...")