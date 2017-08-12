#!/usr/bin/python

i,j = 0,0

while i < 9:
    i += 1
    while j < i + 1:
        j += 1
        print "%d*%d=%d"%(i,j,i*j),
        if i == j:
            j = 0
            print("")
            break
