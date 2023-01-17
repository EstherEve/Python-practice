''' Python is used for web development, math and managing complex code
 Important to note that Python is a case sensitive language 

 Printing to the terminal - similar concept to console in JS '''

print("Hello World") # this is a string as it's in "" marks
print (100) # This is a value as it isn't surrounded by "" marks

# Booleans 
firstNumber = 21
secondNumber = 18
if firstNumber > secondNumber: print ("Have some wine!") # means that the sum above is true

# VARIABLES
# need to be labelled appropriatly, no spaces, case sensitive, no numbers
''' three types
int() WHOLE NUMBER
str() STRING/TEXT
float() DECIMAL NUMBER
'''
string_x = str(3)    # x will be '3' as text
integer_y = int(3)    # y will be 3
float_z = float(3)  # z will be 3.0
# these can be changed to either variable type at any time.

# TYPE OF VARIABLE
print (type(string_x)) # <class 'str'>
print (type(integer_y)) # <class 'int'>
print (type(float_z)) # <class 'float'>

# FYI although the variable names are the same, the lower case firstname makes it a different variable altogether
firstnumber = 17
secondnumber = 18
if firstnumber > secondnumber: print ("Have some wine!")
else: print ("No wine for you")

# simple math
x = 3
y = 6
print (x + y)

a = 5
b = 10 
c = a + b # new variable created and the below will print it
print(c)

