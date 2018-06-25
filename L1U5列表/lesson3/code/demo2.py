# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 10:43
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo2.py

a = [1, 3, 5, 2, 4, 6]
a.sort(reverse = True)
b = sorted(a)
b.append(7)
print("a = %s, b = %s" % (a, b))