# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 10:45
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo3.py

vote = []
flag = True
while flag:
    id = int(input("Please enter the student's number: "))
    if id != 0:
        vote.append(id)
    else:
        flag = False
print("学生1获得选票数 = ", vote.count(1))
print("学生2获得选票数 = ", vote.count(2))
print("学生3获得选票数 = ", vote.count(3))


