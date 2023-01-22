# While Loop - prompt the user to continue to input password until correct. 

userInput = ""
userPassword = "Password123"

while userInput != userPassword:
    userInput = input("Enter Password: ")
    
print("Access granted!")

# Own example, while loop practice - "Who knows me best"

userInput = ""
favFood = "Carbonara"

while userInput != favFood: # HAS to be not equal to operand for this to work - as this condition is true for now
    userInput = input("Your favourite food is: ")

print("You are correct")

# User age AND passCode example:

userAge = 24
ageLimit = 16
passCode = "Password@"
userInput = ""

while userAge >= ageLimit and passCode != userInput: #used the and for two conditions that are true to proceed
    userInput = input("Enter your passcode: ")
print("Access Granted!")

# age input option

userAge = int(input("Enter an Age:\n"))
ageLimit = 18
passCode = "dogcat23"

if userAge >= ageLimit:
    print("You have passed the age check.")
    userCode = input("Enter the Password: ")
    while userCode != passCode:
        userCode = input("Invalid password, try again: ")
    print("Access Granted!")
else:
    print("You haven't passed the age check.")