import math
import random

def FindCommon():
    a = random.sample(xrange(20), 10)
    b = random.sample(xrange(20), 10)

    print "String a: " + str(a)
    print "String b: " + str(b)
    
    common = []
    
    for i in a:
        for j in b:
          if j == i and j not in common:
              common.append(j)

    print "Common Numbers: " + str(sorted(common))
    return

FindCommon()
