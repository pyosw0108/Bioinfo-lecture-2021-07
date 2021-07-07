#! /usr/bin/env python
'''
import sys

if len(sys.argv) != 2:
    print(f"plase add [number]. {sys.argv[0]}")
    sys.exit(1)



try:
    num = int(sys.argv[1])

    if num == 3:
        raise Exception("this is 3")

    print(10/num)
except ValueError as err1:
    print(err1)
    sys.exit(2)
except ZeroDivisionError as err2:
    print(err2)
    sys.exit(3)
except Exception as err3:
    print(err3)
    sys.exit(4)


with open("write_sample.txt", "w") as handle:
    handle.write("hey\n")
    handle.write("hello\n")
'''


file_name = "covid19.fasta"
data = dict()
with open(file_name, "r") as handle:
    for lines in handle:
        if lines.startswith(">"):
            continue
        for base in lines.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)
