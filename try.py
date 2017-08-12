#!/usr/bin/python
#coding=utf-8

def div(a,b):
#try下面可以是一个语句 可以是多个语句  当try捕获到异常时,就执行except后的语句
    try:
        return a / b
#捕获特定异常except后加异常名,不加就捕获异常(所有类型异常) 官方不建议不写特定异常
    except ZeroDivisionError:
        return "zero can not be divsion"
#        不同异常采用不同的处理方式的方法
    except TypeError:
        return "please input the right num"

#     try:
#         return a / b
# #不同的异常采用相同的处理方式的方法,一定要加( )
#     except (ZeroDivisionError,TypeError):
#         return "division error or type error"

result = div(3,0)
#result = div(3,'c')
print result
