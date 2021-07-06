#! /usr/bin/env python
'''
i = input()
while not i.isalpha():
    i = input("again")

i = int(i)

pi = 3.14

print(i*i*pi) # print(i**2*pi)
'''


'''
import math
pi = math.pi



import sys

if len(sys.argv) != 2:

    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

r = int(sys.argv[1])
result = round((r**2*pi), 2)
print(result)
'''

'''
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()

num = int(sys.argv[1])

if num % 2 == 1:
    print(f"This number {num} is odd")
else:
     print(f"This number {num} is even")
'''

'''
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

result = "no"

if num % 3 == 0 and num % 7 == 0:
    result = "3 7"
elif num % 3 == 0:
    result = "3"
elif num % 7 == 0:
    result = "7"

print(result)
'''

'''
val = 1
for i in range(1,11):
    val *= i
print(val)
'''
'''
num = 5
val =  1
while not num == 0:
    val *= num
    num -= 1
print(val)
'''

def greet():
    print("Hello, Bioinformatics")
def greet1():
    print("Hello")
    return 1

greet()
print(greet())
greet1()
print(greet1())

