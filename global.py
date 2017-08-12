#!/usr/bin/python
#coding=utf-8
a = 5
b = 4
def fun():
#globals 是全局变量声明
    global a,b
    a += 1
    b += 1
    print a,b

    c,d = 1,2
# locals 内建函数 收集局部变量 形成返回值 写成字典
    return locals()

print fun()
print a

print globals()
