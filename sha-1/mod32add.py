#!/usr/bin/env python
#-*- coding:utf-8 -*-

import binascii

string = 'abcd'

bin =  hexstr_bin(binascii.b2a_hex(string))
print bin
decimal = int(bin,2)
print decimal
two =  hexstr_bin(binascii.b2a_hex('efgh'))
print two
de = int(two,2)
print de
z = (decimal + de) % 2**32
print z
def base_conv(num,base):
    lis = []
    while True:
        num,rem = divmod(num,base)
        lis.append(rem)
        if num == 0:
            break
    while len(lis) < 32:
	    lis.append(0)		# 保证输出为32位的二进制
    return ''.join([str(x) for x in lis[::-1]]) # -1为逆序
t= base_conv(z,2)
print t
print int(t)
x = 0B01100001011000100110001101100100
y = 0B11000110110010001100101011001100
print
print base_conv(x,2)
print base_conv(y,2)
print base_conv(x^y,2)
def circle_left_shift(x, nbits):
	one = x << nbits
	print one
	two = x >> (32 - nbits)
	print two
	return one & two

print circle_left_shift(1008888888888, 3)
