from datetime import datetime

name = raw_input("What\'s your name?")
age = int(raw_input("What\'s your age?"))

def Calc():
    currentyear = datetime.now().year
    """print currentyear
    """
    
    HowManyYears = 100 - age
    TheYear = currentyear  + HowManyYears
    
    if age == 100:
        print "Aren\'t you already 100...?"
    elif age > 100 and age != 666:
        print "Sorry, bud. You're not getting any younger."
    elif age < 0:
        print "How are you " + str(age) + " years old? That's kind of impossible."
    elif age == 666:
        print ":^)"
    else:
        print name + " will turn 100 on " + str(TheYear)
    return

Calc()

raw_input('Hit enter to finish')
