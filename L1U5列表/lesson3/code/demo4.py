# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 11:27
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo4.py

import random

results = []

for i in range(10000):
    result = random.randint(1, 6)
    results.append(result)

for i in range(1, 7):
    print("%s出现次数 = %s, %s出现频率 = %s" % (i, i, results.count(i), results.count(i) / 10000))




