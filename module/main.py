#!/usr/bin/python
#coding=utf-8
import module1 as m
from module2 import D as m1,b as m2#from 导入到本地命名空间,不能重名
#from module2 import*   导入模块所有的类,不想导入的用被保护的方法在前面加_单下划线
#import module1 #重复调用模块只会执行一次
#reload(module1)#想重复调用需要使用reload

print m.a

obj = m.A()

obj.a()

m.b()

print m.__doc__

print "-----------------------"

obj_d = m1()
obj_d.d()
print m2
