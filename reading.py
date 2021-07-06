#! /usr/bin/env python

#file_name = "read_sample.txt"

#with open(file_name, "r") as handle:
#    for line in handle:
#        print(line.strip())

#handle = open(file_name, "r")
#for line in handle:
#    print(line.strip())
#handle.close()

#handle = open(file_name, "r")
#lines = handle.readlines()
#for line in lines:
#    print(line.strip())
#handle.close()
'''
file_name = "write_sample.txt"
writing = open(file_name, "w")
writing.write("Hello python\n")
writing.write("This is new world!\n")
writing.close()


with open(file_name, "w") as writing:
    writing.write("Hello python\n")
    writing.write("This is new world!\n")

a = "a,b,c"
data = a.split(",")
print(data)

with open(file_name, "a") as handle:
    handle.write("\t".join(data))
    handle.write("\n")
'''
import sys
'''
with open("noname.txt", "r") as fr:
    read = fr.radlines()

print(read)
'''

'''
try:
    num = int(input())
except ValueError as err:
    print(f"{err}, This is not number")
    sys.exit()

try:
    print(10/num)
except ZeroDivisionError as err:
    print(f"{err}, Dont 0")
    sys.exit()
'''

'''
try:
    num = int(input())
    print(10/num)
except ValueError as err1:
    print(f"{err1}, This is not number")
    sys.exit()  
except ZeroDivisionError as err2:
    print(f"{err2}, Dont 0")
    sys.exit()

print(10/num)

class A:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __repr__(self):
        return "this is sachicyeonsan"

a = A("a")
b = A("b")

print(a.val + b.val)
print(a + b)
print(a)


class ValueCalculator:
    def __init__(self, val : str):
        self.val = val

    def __add__(self, other):
        return self.val + other.val
if __name__ == "__main__":
    print("hi")




#covid19 = "covid19.fasta"

#data = dict()

with open(covid19, "r") as sequence:
    for lines in sequence:
        if lines.startswith(">"):
            continue
        for base in lines.strip():
             if base not in data:
                 data[base] = 0
             data[base] += 1
 print(data)

#with open(file_name, "w") as handle:
#    handle.write(lines[1])
'''

import gzip
covid19 = "covid19.fasta.gz"
data = dict()

with gzip.open(covid19, "rb") as sequence:
    for lines in sequence:
        lines = lines.decode("utf-8")
        if lines.startswith(">"):
            continue
        for base in lines.strip():
             if base not in data:
                 data[base] = 0
             data[base] += 1
print(data)
