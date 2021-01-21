import random
DaRange = xrange(1, 11)
List = []
for elem in DaRange:
	List.append(random.randint(1, 5))
def SortLst():
	SortedSet = set(List)
	SortedList = list(SortedSet)
	return SortedList
	
print List
print SortLst()

raw_input("Press enter to end program...")