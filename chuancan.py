#!/usr/bin/python
#coding=utf-8

def fun(a,b):
    print a,b

#位置传参
fun(1,2)

#关键字传参
fun(b = 1,a = 2)

# * 传参 将数组中的值进行位置传参
l = [5,6]
fun(*l)

# ** 传参 将字典中键的值对应位置传参

d = {'b':1,'a':2}
fun(**d)
