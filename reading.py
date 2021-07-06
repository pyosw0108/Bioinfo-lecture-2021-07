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

with open("noname.txt", "r") as fr:
    read = fr.radlines()

print(read)
