#!/usr/bin/python
#coding=utf-8
def div(a,b):
    try:
        #return a / b
        c = a / b
    except ZeroDivisionError as e: #as e 这个异常的结果赋予e 这个e是自己定的什么字符都可以
        return e
    except TypeError as e:
        return e
    else:
        print "else.............."
    finally:
        print "finally............"

    return c

result = div(3,1)
# result = div(3,0)
# result = div(3,'c')
print result
