#2 - Variables, expressions, statements, and functions

#Assignment statements

message = "And now for something completely different"
n = 17
pi = 3.141592653589793

#String Operations

first_variable = "Muzy"
last_variable = "1463"

print(first_variable + ' ' + last_variable) #prints Muzy 1463

print("Muzy"*4) #MuzyMuzyMuzyMuzy

x = y = 2

print(x) #2
print(y) #2

y = 3
print(x) #2
z = 3
print(z)

#Functions

print(int(4.3)) #4
print(int(-2.3)) #-2

print(float(3)) #3.0
print(float(-2)) #-2.0
print(str(4)) #"4"

import math

first_number = math.sqrt(9)
second_number = math.log10(100)
third_number = math.sin((30/180)*math.pi)

print(first_number) #3.0
print(second_number) #2.0
print(third_number) #0.49999999999999994

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#Parameters and arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice(23) #23 here is the argument, bruce is the parameter.

#Variables and parameters are local

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

#When cat_twice terminates, the variable cat is destroyed. If we try to print it, we get an exception:

print(cat)