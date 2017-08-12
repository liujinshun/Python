#!/usr/bin/python
#coding=utf-8

shuzi = 5
cishu = 3
print('------猜数字游戏！-----')
a = 0
while (a != shuzi) and (cishu > 0):
    t = input('猜数字游戏开始，请输入数字：')
    a = int(t)
    cishu -= 1
    if a == shuzi:
        print('恭喜，您猜对了！')
    else:
        if a > shuzi:
            print('您输入的数字大了！')
        else:
            print('您输入的数字小了！')
print('游戏结束，再见！^_^')
