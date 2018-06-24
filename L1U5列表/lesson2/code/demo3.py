# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 16:21
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo3.py

nums = list(range(100, 1001))
for a in nums:
    b = str(a)
    flag = True
    for i in range(len(b)):
        if b[i]!=b[len(b)-i-1]:
            flag = False
    if flag:
        print("%s是回文数" % (b))








