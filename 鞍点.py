#!/usr/bin/python
#coding=utf-8
l = [[5,2,7,3],[4,9,2,8],[5,1,6,7]]
outLen = len(l)
inLen = len(l[0])

for i in l:
    for j in i:
        print j,
    print ""


for i in l:
    m = max(i)
    n = i.index(m)
    j = 0
    while j < len(l):
        if l[j][n] > m:
            break
        j += 1
    else:
        print i[n]
