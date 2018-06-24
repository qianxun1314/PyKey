# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 14:44
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py

vote = [0, 0, 0]
flag = True
while flag:
    id = int(input("Please enter the student's number: "))
    if id != 0:
        vote[id-1] += 1
    else:
        flag = False
print(vote)

