import time


print('Greetings! Whats your first name')

firstName = input()
fNameLength = len(firstName)


print("okay so your first name is "+ firstName + " and, fun fact, your first name is " + str(fNameLength) + " characters long")

i=0
while i < len(firstName):
    print(firstName[i], end=' ')
    i += 1

#time.sleep(3)

#print(f"{firstName}{fNameLength}")

# print(firstName + " what is your LAST name?")
# lastName = input()
# print("Nice! " + firstName + " " + lastName + " huh?")
# print("your initials are " + firstName[0] + "." + lastName[0] + ".")

