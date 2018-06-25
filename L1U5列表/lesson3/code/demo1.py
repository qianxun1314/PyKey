# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 09:30
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py

a = [3, 4, 16, 1, 7, 10]

max = a[0]
for i in a[1:]:
    if i > max:
        t = i
        i = max
        max = t

print("max = ", max)