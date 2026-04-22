########################################
# Basic IO operations

print("Hello")

########################################
# print() function

print("123")    # gives 123
print(123)      # gives 123
print()         # gives an empty line
print("abc")    # gives abc
print(abc)      # raises Error

########################################
# Variables

xyz = 456       # here xyz is a variable

print("xyz")    # gives xyz, prints it as it is
print(xyz)      # gives 456, prints the value of xyz

########################################
# input() function

xyz = input()   # here xyz is a variable

print("xyz")
print(xyz)

########################################

name = "Rancho"
# print multiple values in multiple lines
print("Hello")
print(name)
print("How are you?")
print()
# print multiple values in the same line by separating them using commas
print("Hello",name," How are you?")
print()
# print multiple values in the same line by using f-strings
print(f"Hello {name} How are you?")

########################################
# type() function

var = 12
print(type(12))
print(type(var))
print()

var = 3.4
print(type(3.4))
print(type(var))
print()

var = "56"
print(type("56"))
print(type(var))
print()

var = True
print(type(var))
print(type(True))

########################################

name = input("Enter your name: ")
print(f"value = {name}, type = {type(name)}")

number = input("Enter a number: ")
print(f"value = {number}, type = {type(number)}")

########################################
# Type casting

a = input("Enter a number: ")
print(f"value = {a}, type = {type(a)}")

a = int(a)
print(f"value = {a}, type = {type(a)}")

########################################

a = input("Enter a number: ")
b = input("Enter another number: ")

print(f"Before typecasting: {a} + {b} = {a + b}")

a = int(a)
b = int(b)

print(f"After typecasting : {a} + {b} = {a + b}")

########################################
# Arithmetic operators
# - Inputs are numbers
# - Output is number
# [`+`, `-`, `*`, `/`]

a = 22
b = 7

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

########################################
# Relational operators
# - Inputs are numbers
# - Output is boolean
# [`==`, `!=`, `<`, `>`, `<=`, `>=`]

a = 2
b = 7

print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}")
print(f"{a} <  {b} = {a < b}")
print(f"{a} >  {b} = {a > b}")

########################################
# Logical operators
# - Inputs are boolean
# - Output is boolean
# [`not`, `and`, `or`]

a = True
b = False

print(f"not {a} = {not a}")
print(f"not {b} = {not b}")
print()
print(f"{a} or  {b} = {a or b}")
print(f"{a} and {b} = {a and b}")

########################################
# Conditions
# - Expressions that result in a boolean value (i.e. either True or False).
# - These are used to alter the flow of the program at runtime.

a = 4
b = 5

a_is_positive = a > 0
b_is_positive = b > 0
both_positive = a_is_positive and b_is_positive

print(f"Is a positive?      {a_is_positive}")
print(f"Is b positive?      {b_is_positive}")
print(f"Are both positive?  {both_positive}")

########################################
# Conditional statements
# These statements allow us to take decisions at runtime,
# based on some condition.

########################################
# if statement

condition = False

print(1)

if (condition):
    print(2)
    print(3)

print(4)

########################################
# else statement

condition = False

print(1)

if (condition):
    print(2)
else:
    print(3)

print(4)

########################################
# if-elif-else statement

condition1 = True
condition2 = True
condition3 = True

print(1)

if (condition1):
    print(2)

elif(condition2):
    print(3)

elif(condition3):
    print(4)

else:
    print(5)

print(6)

########################################
# while loop

count = 0

print(f"Before : {count}")

while (count < 5):
    print(f"Inside : {count}")
    count = count + 1

print(f"After  : {count}")

########################################
# We have to search for an unknown number
# selected by a person in a given range (say 1 to 100).
# After each guess, the other person will reply with either or these:
# - my number is higher than your guess
# - my number is lower than your guess
# - my number is equal to your guess
# Based on the response, you have to make a new guess.
# The game continues until you find the correct number.

########################################
# **Approach 1** (Linear Search)
# Check for each number in the given range,
# starting from the lowest to the highest,
# until you find the correct number.
# As you can see, this is going to be very slow.

lower_bound = 1
upper_bound = 100

print(f"Think of a number between {lower_bound} and {upper_bound}")

guess = lower_bound
match_found = False

while(guess <= upper_bound and not match_found):
    print(f"My guess is {guess}")
    response = input("Select response (< = >): ")
    guess = guess + 1

    if(response == "="):
        print("I won!")
        match_found = True
        break

########################################
# **Approach 2** (Binary Search)
# Instead of checking of all numbers from start till end,
# we check for the middle number. This will result in 3 cases:
# - it matches with the unknown number:
#       we win
# - its lower the unknown number:
#       in this case will eliminate the lower half of the range
# - its higher the unknown number:
#       in this case will eliminate the upper half of the range
# So just a simple guess will reduce the range by half.

lower_bound = 1
upper_bound = 100

print(f"Think of a number between {lower_bound} and {upper_bound}")

match_found = False

while(lower_bound <= upper_bound and not match_found):
    guess = (lower_bound + upper_bound) // 2

    print(f"My guess is {guess}")
    response = input("Select response (< = >): ")
    if(response == "<"):
        upper_bound = guess - 1
    elif(response == ">"):
        lower_bound = guess + 1
    elif(response == "="):
        print("I won!")
        match_found = True
        
########################################
# String Operations

myName = "Rancho"
print(f"value = {myName}")
print(f"type  = {type(myName)}")

########################################
# Escape Sequences
# - `\t` : for long space
# - `\n` : for new line

print("I want to\tlearn Python\nIts a programming language.")

########################################
# len() function

myString = "Programming Language"
length = len(myString)
print(f"No of characters = {length}")

########################################
# 0-based indexing

myString = "Python"
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])
print(myString[5])

########################################
# Negative indexing

myString = "Python"
print(myString[-1])
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])
print(myString[-6])

########################################
# Changing case

myString = "RaNch0!?"
print(f"{myString.lower()}")
print(f"{myString.upper()}")

########################################
# Substring check

myString = "the cat sat on the mat"

print("cat" in myString)
print("at" in myString)
print("dog" in myString)
print()
print(myString.count("cat"))
print(myString.count("at"))
print(myString.count("dog"))
print()
print(myString.index("cat"))
print(myString.index("at"))
if("dog" in myString):
    print(myString.index("dog"))    # raises Error if "dog" isn't in myStr
else:
    print("dog not found")

########################################
# List & Dictionaries

myList = [5, 2, 1, 4]       # to store values
print(f"value = {myList}")
print(f"type  = {type(myList)}")
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1} # to store key:value pairs
print(f"value = {myDict}")
print(f"type  = {type(myDict)}")

########################################
# len() function

myList = [5, 2, 1, 4]
print(f"value = {myList}")
print(f"len   = {len(myList)}")
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}
print(f"value = {myDict}")
print(f"len   = {len(myDict)}")

########################################
# Indexing in lists

myList = [5, 2, 1, 4]
# 0-based indexing
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
# negative indexing
print(myList[-1])
print(myList[-2])
print(myList[-3])
print(myList[-4])

########################################
# Indexing in Dicts

# myList = [5, 6, 4]
myDict = {'Eng': 5, 'Sci': 6, 'Mat': 4}
# Key based indexing
print(myDict['Eng'])
print(myDict['Mat'])
print(myDict['Sci'])

########################################
# Membership check

myList = [5, 2, 1, 4]
print(5 in myList)  # slow
print(6 in myList)  # slow
print()

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}
print('Eng' in myDict)      # fast
print(5 in myDict)      
print(5 in myDict.values()) # slow

########################################
# Adding new items

myList = [5, 2, 1, 4]

print(myList)
myList.append(7)
print(myList)
myList.insert(1, 8)
print(myList)

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1}

print(myDict)
myDict['Sst'] = 4
print(myDict)

########################################
# Deleting existing items

myList = [8, 1, 4, 2, 0]

print(myList)
myList.pop(3)
print(myList)

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1, 'SSt': 4}

print(myDict)
myDict.pop('Mat')
print(myDict)

########################################
# For loop on string

myString = "Loop"
for ch in myString[1:3]:
    print(f"I am currently looking at {ch}")
print("Loop stopped!")

########################################
# For loop on list

myList = [8, 1, 4, 2, 0]
for num in myList:
    print(f"I am currently looking at {num}")
print("Loop stopped!")

########################################
# For loop on dictionary

myDict = {'Eng': 5, 'Mat': 2, 'Sci': 1, 'SSt': 4}
for key in myDict:
    print(f"I am currently looking at {myDict[key]}")
print("Loop stopped!")

########################################
# Running a loop for specified number of times

N = 4
for i in range(N):
    print(f"Hello {i}")
print("Loop stopped!")

########################################
# Nested Structures
# - We can store lists or dictionaries inside other lists or dictionaries
# - Structures liked these are called nested structures

########################################
# list of lists

nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested[0])}")
print()
print(nested)
print(nested[1])
print(nested[1][2])

########################################
# list of dicts

nested = [
    {'name':'Ronaldo', 'country':'Por', 'age':40},
    {'name':'Messi',   'country':'Arg', 'age':37},
    {'name':'Neymar',  'country':'Brz', 'age':30},
    {'name':'Ramos',   'country':'Spn', 'age':39},
]
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested[0])}")
print()
print(nested)
print(nested[1])
print(nested[1]['name'])

########################################
# dict of lists

nested = {
    'names' : ['Ronaldo', 'Messi', 'Neymar', 'Ramos'],
    'countries' : ['Por', 'Arg', 'Brz', 'Spn'],
    'ages' : [40, 37, 30, 39]
}
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested['names'])}")
print()
print(nested)
print(nested['names'])
print(nested['names'][2])

########################################
# dict of dicts

nested = {
    'left_forward' : {
        'name':'Ronaldo', 'country':'Portugal', 'age':40
    },
    'right_forward' : {
        'name':'Messi', 'country':'Argentina', 'age':37
    },
    'mid_fielder' : {
        'name':'Neymar', 'country':'Brazil', 'age':30
    },
    'center_back' : {
        'name':'Ramos', 'country':'Spain', 'age':39
    }
}
print(f"type of structure = {type(nested)}")
print(f"type of elements  = {type(nested['left_forward'])}")
print()
print(nested)
print(nested['left_forward'])
print(nested['left_forward']['name'])

########################################
# Functions
# - A function is control block in programming language that performs a specific task
# - A function can have zero, one or more parameters (inputs)
# - A function can have zero, one or more return values (outputs)

########################################
# NO parameter, NO return value

def greet():
    print("Hello")

x = greet()
print(x)

########################################
# ONE parameter, NO return value

def greet(name):
    print(f"Hello {name}")

x = greet("Rancho")
print(x)

########################################
# NO parameter, ONE return value

def greet():
    print("Hello")
    return 7

x = greet()
print(x)

########################################
# ONE parameter, ONE return value
 
def greet(name):
    print(f"Hello {name}")
    return 7

x = greet("Rancho")
print(x)

########################################
# Function to find the greater of the two numbers

def max(a, b):
    if (a > b):
        return a
    else:
        return b
    
x = max(10, 20)
print(f"ans = {x}")

x = max(20, 10)
print(f"ans = {x}")

########################################