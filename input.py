import random
colorlist = ['orange', 'red', 'blue', 'yellow', 'turqoise', 'black', 'white', 'green']
print("Hello there!")
name = input("What is your name? ")
print("Nice to meet you",name,"!")
color = input("Here's a question for you...What is your favorite color? ")
print(name, "your favorite color is", color)
print("My favorite color is", random.choice(colorlist))