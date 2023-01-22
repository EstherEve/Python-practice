''' CREATED A MENU WITH SUBJECT OPTIONS THAT THE USER CAN SELECT (A USER INPUT FEATURE), WHICH WILL PRINT 
THEIR SUBJECT RESULT '''

print(
    '''
    Language option menu
    1. French
    2. Spanish 
    3. Italian
    4. Yuroba
    5. Twi
    '''
)

selection = input("Enter the language you would like to learn: ")

if selection == "1": # first condition
    print("You have selected French")
elif selection == "2": # section condition etc...
    print("You have selected Spanish")
elif selection == "3":
    print("You have selected Italian")
elif selection == "4":
    print("You have selected Yuroba")
elif selection == "5":
    print("You have selected Twi")
else:
    print("Exiting Program.")

# NESTED IF statement 

# Private Members club example

memberAge = 21
ageLimit = 18
entryPassword = "Dior"

if memberAge >= ageLimit: #First condition which will proceed to nested if section if returns true
    print("Passed the first door") # first true outcome message 
    entryPassword = "Jackson" # variable to match to pass next condition. NOTE - we have input this ourselves
    if entryPassword == "Dior": # entryPasswords need to be ==(equal to) "Dior"
        print("Come through!") #Next true outcome message 
    else:
        print("Nice Try, Goodbye!") # in this case they are over 18, BUT wrong password 
else:
    print("Not old enough") # if first condition returns faulse, it will come here 
    
# NESTED IF - USER INPUT 

memberAge = 21
ageLimit = 18
entryPassword = "Dior"

if memberAge >= ageLimit: #First condition which will proceed to nested if section if returns true
    print("Passed the first door") # first true outcome message 
    entryPassword = input("Entry password please: ") #allows user to input the entry password 
    if entryPassword == "Dior": # entryPasswords need to be ==(equal to) "Dior"
        print("Come through!") #Next true outcome message 
    else:
        print("Nice Try, Goodbye!") # in this case they are over 18, BUT wrong password 
else:
    print("Not old enough") # if first condition returns faulse, it will come here 