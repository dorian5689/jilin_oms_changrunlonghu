#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/26 19:25
@Auth ： Xq
@File ：1.py
@IDE ：PyCharm
"""

with open("1.txt","a+",encoding="utf-8" ) as f:
    for i in range(10):
        f.write(str(i)+"\n")