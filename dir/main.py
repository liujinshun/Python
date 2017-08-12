#!/usr/bin/python

import dir1.module1
from dir1 import module2

print dir1.module1.a

obj = dir1.module1.A()

obj.a()
dir1.module1.b()
a = 10
print dir1.module1.__doc__

print "---------------------"

obj_d = module2.D()
obj_d.d()
print module2.b
