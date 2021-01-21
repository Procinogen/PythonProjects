import random
"""
a = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
b = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
"""
a = random.sample(range(1,20), 10)
b = random.sample(range(1,20), 15)
c = [elem for elem in a if elem in b]

print "String a: " + str(a)
print "String a: " + str(b)
print "Common Elements: " + str(c)
