# IF STATEMENTS AND CONDITIONS

ring1 = 1000
ring2 = 800
if ring1 > ring2:
    print("Let's get married!")
else: 
    print("Try again!")

# Tip:
# Make sure there is a semi-colon after condition and else. 
# Sytax - Also else needs to be in line with if, or there will be an error in the code 

# ELIF (Else-if)

score = 625

grade = "" # converting the value to string/text for output
if score > 800:
    grade = "A"
elif score > 600:
    grade = "B"
elif score > 300:
    grade = "C"
print("Here is your final grade: ", grade)
