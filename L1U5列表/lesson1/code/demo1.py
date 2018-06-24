# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 10:55
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py


sum = 0

for i in range(101):
    if i % 2 == 0 and i % 3 == 0:
        sum += i

print("sum = ", sum)