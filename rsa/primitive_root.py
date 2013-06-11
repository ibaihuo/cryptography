#!/usr/bin/env python
#-*- coding:utf-8 -*-

import bigmod

prime = int(raw_input ('please input a prime(100 < prime < 1000):'))
#prime = 101
primitive_root = []
for a in range(1, prime):
    res = []
    for i in range (1, prime):
        res.append(bigmod.bigmod(a, i, prime))
    res_single = set(res)                      # remove the duplicate members
    if len(res) == (prime -1) and len(res_single) == (prime -1):
        #print a,res_single
        primitive_root.append(a)        # get the primitive root

print 'The primitive root are: ', primitive_root
print 'The number of primitive root:', len(primitive_root)
