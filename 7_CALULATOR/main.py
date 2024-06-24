import math 
def add(a,b):
    print(f"The Addition of {a} and {b} is {a+b}")

def sub(a,b):
    print(f"The Subtraction of {a} and {b} is {a-b}")

def mul(a,b):
    print(f"The Multiplication of {a} and {b} is {a*b}")

def div(a,b):
    print(f"The Division of {a} and {b} is {a//b}")

def expo(a,b):
    print(f"The power {b} of the number {a} is {a**b}")

def fact(a):
    fib = 1
    for i in range(a,0,-1):
        fib = fib * i
    print(f"The Factorial of {a} is {fib}")

def root(a):
    print(f"The Square root of {a} is {math.sqrt(a)}")


def main():
    calu = input("Choose Any one of the following:\nA)Addition\nB)Subtraction\nc)Multiplication\nD)Division\nE)Exponent\nF)Fatorial\nG)Square_root\n: ")
    if calu in ['a','A','1']:
        a = int(input("Enter 1st Operand: "))
        b = int(input("Enter 2nd Operand: "))
        add(a,b)
    elif calu in ['b','B','2']:
        a = int(input("Enter 1st Operand: "))
        b = int(input("Enter 2nd Operand: "))
        sub(a,b)

    elif calu in ['c','C','3']:
        a = int(input("Enter 1st Operand: "))
        b = int(input("Enter 2nd Operand: "))
        mul(a,b)

    elif calu in ['d','D','4']:
        a = int(input("Enter Divident "))
        b = int(input("Enter Divisor: "))
        div(a,b)

    elif calu in ['e','E','5']:
        a = int(input("Enter a number: "))
        b = int(input("Enter a power the previous number: "))
        expo(a,b)

    elif calu in ['f','f','6']:
        a = int(input("Enter a number: "))
        fact(a)

    elif calu in ['g','G','7']:
        a = int(input("Enter a number: "))
        root(a)

if __name__ == "__main__":
    main()