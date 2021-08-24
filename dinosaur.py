# First lines of code
print("Hello World")
print("monkey man the great destroyer")
print("i will beat nathan and destroy that kid")

# Drawing a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables and Data Types - basically variables store
character_name = "nathan"
character_role = "genius"
character_age = 69.9999999
# numbers don't have to be in quotations
# strings are basically the data in quotations ""

print("There once was a programmer named " + character_name + ", ")
print("He was a " + character_role + ".")
# can edit it like this and split a story
character_role = "idiot"
print("But i will destroy that " + character_role + ".")
print("He cannot beat me")


# a bullient value? what the fuck
is_male = False
is_female = True


# Working with strings
# \n splits the string into the second line
print("Monkey Man\nThe Great Destroyer")

# backslash \ in strings can render literally
print("Nathan \"Genius\" Monkey")

# can store variables into a phrase
phrase = "\"Justice is subject to dispute, but might is easily recognized and not disputed.\""
print(phrase)

# can add upon a phrase utilizing a plus sign this is called concatenation
phrase = "\"I just keep moving forward until my enemies are destroyed\""
print(phrase + " - Eren Yeager")

# functions are a block of code that you can run
phrase = "DUMBASS YOU SUCK"
print(phrase.lower())

phrase = "please be quiet"
print(phrase.upper())

# can also utilize functions with is to check if true or false
phrase = "MONKEYMAN"
print(phrase.isupper())
phrase = "MONKEYMAN"
print(phrase.islower())
# utilizing periods/dots with functions allows you to combine their use
phrase = "monkeyman"
print(phrase.upper().isupper())
# figuring out the length of a string
phrase =  "dinosaurs will be extinct."
print(len(phrase))
# grabbing something from a string, python starts strings at 0 value
phrase = "dinosaurs will be extinct."
print(phrase[0])

# indexes allow you to pass parameters - basically telling you to location where a variable is
phrase = "dinosaurs will be extinct."
print(phrase.index("d"))
print(phrase.index("extinct"))
# can tell you where it starts even a word

phrase = "Might is subject to dispute; might is easily recognized and not disputed."
print(phrase.replace("Might", "Justice"))
# how the fuck do you replace two variables at once in the same sentence without creating two sentences?

print(-69.99999999999999999999999)
print(9+10)
# order of operations bedmas
print(3 * (4 + 5))

# modulus operator - basically gives the remainder after it divides
print(10 % 3)
print(24 % 4)

my_num = 5
print(my_num)
# how to convert a number into a string
print(str(my_num) + " my favourite number")
# if you didn't convert the number into a string = error

# functions with numbers
# ABS = absolute value
my_num = -69
print(abs(my_num))
print(pow(6, 9))
print(pow(2, 2))
# tells you which number is bigger - max function
print(max(4, 6))
print(round(3.2))
print(round(69.9))

# importing external code, python math etc - from math import *

from math import *
my_num = -5
print(floor(3.7))
# floor grabs the lowest number out of 3 or 7 in 3.7
print(ceil(3.9))
# ceil rounds the number no matter what
print(sqrt(4))
# sqrt finds square root
# from math import * is basically a module


# Getting Input From Users - name stores the input, while input prompts the user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + ".")

