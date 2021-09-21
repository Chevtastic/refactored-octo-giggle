
print("Greetings! What's your first name")

firstName = input() # get user input for first name
fNameLength = len(firstName) #get length of first name
capitalFirst = firstName.capitalize() #capitalize first name

print("okay so your first name is " + capitalFirst + "\nhere's a fun fact, your first name is " + str(fNameLength) + " characters long")

#While loop to spell out each letter 
i=0
while i < len(firstName):
    print(capitalFirst[i])#, end=' ')
    i += 1


# trying out f strings but commenting out for this project
# print(f"{firstName} {fNameLength}")

print( capitalFirst + " what is your LAST name? ") 

lastName = input() #get user last name
lNameLength = len(lastName) #get length of last name
capitalLast = lastName.capitalize() #capitalize first letter
fullName = (capitalFirst + " " + capitalLast) 
fullLength = len(lastName) + len(firstName)

print("Nice! " + capitalFirst + " " + capitalLast + " huh?")
print("your last name is " +str(lNameLength)+ " characters long and your full name is " + str(fullLength) + " characters long")
print("your initials are " + capitalFirst[0] + "." + capitalLast[0] + ".")
print("it was nice to meet you " + fullName)


