# Subroutines - similar to a function. It is a group of code that can be used again using it's key word

# Syntax: def identifier():

def helloWorld():
    print("Hello World")
    print("My name is Esther")
    print("I love to code")
    # => Nothing will happen just with this group of code. We need to 'invoke' the function by adding the keyword.

helloWorld() # Tip - ensure that when invoking the subroutine, call outside of the sub group. 

# addition 

def addition():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    answer = num1 + num2
    print(answer)
addition()

# subtraction 

def subtraction():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    answer = num1 - num2
    print(answer)
subtraction()

# multiplication

def multiply():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    answer = num1 * num2
    print(answer)
multiply()

# division

def divison():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    answer = float(num1 / num2) # float is the default unless int is specified 
    print(answer)
divison()