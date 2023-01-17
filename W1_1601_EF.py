''' Python is used for web development, math and managing complex code
 Important to note that Python is a case sensitive language 

 Printing to the terminal - similar concept to console in JS '''

print("Hello World") # this is a string as it's in "" marks
print (100) # This is a value as it isn't surrounded by "" marks

# Booleans 
firstNumber = 21
secondNumber = 18
if firstNumber > secondNumber: print ("Have some wine!") # means that the sum above is true

choice = True
oChoice = False
print(type(choice)) # => <class 'bool'>

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

print (7 * 10) # => math within the terminal instantly

x = 3
y = 6
print (x + y) # => math using values assigned to 

a = 5
b = 10 
c = a + b # new variable created and the below will print it
print(c)

fNumber = input()
sNumber = input()

# STRING TO NUMBER

numb1 = input("Enter first: ")
numb2 = input("Enter second: ")
sum = int(numb1) + int(numb2)
print(sum)

# STRING TO FLOAT

numb1 = input("First number: ")
numb2 = input("Second number: ")
sum = float(numb1) / float(numb2)
print(sum)

#checking data types

fName = "Esther"
age = 28
PI = 3.14
print(type(fName)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(PI)) # <class 'float'>

# Other Data Type
# Lists, Tuples, Dictionaries

# Lists [SquareBrackets]
# Zero Indexing | Zero-Based Numbering:
#		  0		1	2	 3		4
myList = [150, 341, 458, 3945, 298]
print(myList)
print(myList[2])
print(myList[2] + myList[4])

fifthItem = myList[4]
print(fifthItem)

myList.insert(2, 700)
myList.append("Ive got you in my sights")
myList.remove(150)
myList.pop(5)

print(myList)


# Tuples (RoundBrackets)
myTuple = (250, 294, 49, 5491, 519) # Immutable: Cant change the values after definition
print(myTuple)

print(myTuple[4])

# Dictionaries {Curly Brackets}
# Key:Value Pair

# ACCESSING ITEMS WITHIN DICTIONARY 

thisIsMe = {
    "firstName" : "Esther",
    "lastName" : "Francique",
    "location" : "London",
    "bio" : "Software Developer"
}

print(thisIsMe["bio"]) # => Software Developer

# Tips 
''' 
- ensure that the text have quotes arount them
- remember the commas after each section
- square brackets only, with the name of the title section in ""
'''

