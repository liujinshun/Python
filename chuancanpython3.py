#!/usr/bin/python3
#coding=utf-8
#python3 中 传参顺序关键字传参可以在元组传参后面
def fun(a,b = 100,*c,d):
    print (a)
    print (b)
    print (c)
    print (d)

fun(1,2,3,4,d = 5)
