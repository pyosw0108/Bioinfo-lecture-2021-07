#! /usr/bin/env python
'''
seq1 = "ATGTTATAG"
r_seq1 = ''
d_base = {"A":"T", "T":"A", "G":"C", "C":"G"}

for i in seq1:
    r_seq1 += d_base[i]
print(r_seq1)


for i in range(len(seq1)):
    s = seq1[i]
    cs = r_seq1[i]
    bond = "≡"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{s}")
'''

'''
seq1 = "AGTTTATAG"
for i in range(len(seq1)-1):
    if seq1[i] == "T" and seq1[i+1] == "T":
        print(i)
'''

data = [3,1,1,2,0,0,2,3,3]
data.sort()
cnt = {}
for elem in data:
    if elem not in cnt:
        cnt[elem]=0
    cnt[elem] += 1

print(cnt)
