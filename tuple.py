#!/usr/bin/python
#coding=UTF-8
#元组中只包含一个元素时,元素后面加逗号
t1 = ('python','hello',1996,2000,)
t2 = (1,2,3,4,5,6,7,)
print "t1[0]:",t1[0]#元组可以进行截取,组合,下标索引从0开始
print "t2[1:5]",t2[1:5]
t3 = t1 + t2 # 元组中元素不允许修改,但可以对元组连接组合
print "t3:",t3