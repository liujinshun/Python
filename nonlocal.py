#!/usr/bin/python3
#coding=utf-8

a = 1

def out():
    b = 2
    def inner():
        nonlocal b
        b += 1
        print (b)
    inner()


out()
