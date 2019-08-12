statement = "please enter a number\n"
def Addition(a, b):
    addit = a + b
    print("Addition is ", addit)

def Subtraction(a, b):
    addit = a - b
    print("Subtraction is ", addit)

def Multiplication(a, b):
    addit = a*b
    print("Multiplication is ", addit)

def Division(a, b):
    addit = a/b
    remainder = a%b
    print("quotient is ", addit , " remainder is ", remainder)

def Square(a):
    addit = a*a
    print("square number of ", a, " is ", addit)


def Handler():
    a = int(input(statement))
    b = int(input(statement))
    ope = str(input("Please enter first three letters of the operation that you want to do, for example for addition type add \n"))
    if(ope == "add"):
        Addition(a, b)
    if(ope == "sub"):
        Subtraction(a, b)
    if(ope == "mul"):
        Multiplication(a, b)
    if(ope == "div"):
        Division(a, b)
    if(ope == "squ"):
        Square(a)
    if(ope == "exi"):
        quit()
    else:
        print("Please try again")
        Handler()
Handler()

