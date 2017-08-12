#!/usr/bin/python
#coding=utf-8
# 类名首字母大写
class Person(object):
    def __init__(self,name):
        self.name = name

    age = 10

#第一位self不传参
    def color(self,c):
        print "%s is %s,he is %d"%(self.name,c,self.age)


boy1 = Person("Jame")

boy1.age = 12

print boy1.age

print boy1.name
boy1.face = "帅"
boy1.color("block")
print boy1.face

print "-------------------------"

boy2 = Person("Lilei")

print boy2.age

print boy2.name

boy2.color("write")

print "----------------------------"

print Person.age
