#!/usr/bin/python
#coding=utf-8
x = 5

print '您最多有三次猜数字的机会'
for i in range(3):
    r = input()
    if r>x:
        print '猜大了,还剩',3-i-1
    elif r<x:
        print '猜小了,还剩',3-i-1
    else:
        print '猜中了'
        break
print '猜数字游戏结束'
