#!/usr/bin/python
#coding=utf-8
l = [[5,2,7,3],[4,9,2,8],[5,1,6,7]]
outLen = len(l)
inLen = len(l[0])

for i in l:
    for j in i:
        print j,
    print ""


i = j = 0
x = y = 0
max = l[0][0]

while i < outLen:
    j = 0
    while j < inLen:
        if l[i][j] > max:
            max = l[i][j]
            x,y = i,j

        j += 1
    i += 1

print "l[%d][%d] = %d"%(x,y,max)
