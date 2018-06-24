# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 15:57
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo2.py


a = [1, 3, 6, 7, "g", "h"]
b = [0, 4, 5, 6, 7, 9, "a", "h", "k"]

c = [1, 3, 6, 7, "g", "h"]
for i in a:
    if i in b:
        c.remove(i)
print(c)
