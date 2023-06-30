#Conditionals and recursion

#floor division
minutes = 105
print(minutes//60) #floor division, returns 1

#modulus operator

remainder = minutes % 60
print(remainder)

#boolean expressions

print("X" == "Y") #Prints False

print(1 == 0) #Prints False

print(1 == True) #Prints True

x = 4
y = 4

print(x == y) #True
print(x is y) #True

print(42 and True) #prints True
print(0 and 50) #prints 0.


#Conditional Execution

# Example 1
x = 5

if x > 0:
    print("X is greater than 0")

else:
    print("No")

# Example 2
y = True

if y:
    print("Y is True")
else:
    print("Y is False")

# Example 3
if x == y:
    print("X equals Y")

elif x > y:
    print("X is bigger than Y")

else:
    print("X is less than Y")

# Example 4

a = 1
b = 2

if a > b:
    print("A is bigger than B")

else:
    if a < b:
        print("A is less than b")

    else:
        print("They are equals")

# Example 4

z = 10
if 9 < z < 11:
    print("Z must be within the range (9,11)")

# Recursion

def countdown(n):
    if n <= 0:
       print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

#Inputs

text = input("Type something: \n")

print("Here's what you typed: " + text)