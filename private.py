#!/usr/bin/python
#coding=utf-8
class Parent(object):
    def __init__(self):
        self.job = "teacher"
        self.__name = 'cainiao'

    def name(self,n): #赋予一个权限
        if n == 1:
            return self.__name
        else:
            return "sorry"

class Child(Parent):
    pass


p = Parent()
print p.job
print p.name(1) #赋予一个权限
