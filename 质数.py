#!/usr/bin/python

n,d = 3,3
for n in range(0,100):
    n += 1
    for d in range(0,100):
            d += 2
            if n % d == 0:
                break
    if d == n:
        print "%d" %n
