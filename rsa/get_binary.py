#!/usr/bin/env python
#-*- coding:utf-8 -*-

rem = []
p = 29
while p:
    rem.append(p & 1)                   # get the last bit
    p >>= 1                             # shift right one bit
print rem
rem.reverse()                           # resverse the list
print rem
