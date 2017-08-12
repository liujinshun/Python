#!/usr/bin/python
#coding=utf-8

def fun(a,b = 100,*c):
    print a
    print b
    print c

fun(1,2,3,4,5)

print "------------------------"
#  函数传参的传递顺序  常规传参>>默认值传参>>元组中位置传参>>字典中位置传参
def fun1(a,b = 100,*c,**d):
    print a
    print b
    print c
    print d

fun1(1,2,3,4,5,c = 6 ,d = 7)
