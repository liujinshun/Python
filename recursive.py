#!/usr/bin/python
#coding=utf-8
#求5的阶层
def recursive(n):
    if n < 1:
        return 1
    return (n * recursive(n - 1))

r = recursive(5)

print "5! = %d"%r
