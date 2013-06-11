#!/usr/bin/env python
#-*- coding:utf-8 -*-

# convert a hex-string to it's bin code
# return the bin code
# retury type: str
def hex_bin(hex_str):
    """convert hex-str to it's bin code
    """
    hex_bin_map={ '0':'0000',
                  '1':'0001',
                  '2':'0010',
                  '3':'0011',
                  '4':'0100',
                  '5':'0101',
                  '6':'0110',
                  '7':'0111',
                  '8':'1000',
                  '9':'1001',
                  'a':'1010',
                  'b':'1011',
                  'c':'1100',
                  'd':'1101',
                  'e':'1110',
                  'f':'1111'}
    return ''.join((hex_bin_map[x] for x in hex_str)) # return the converted code

def dec_bin(num, nbits):
    """返回10进制数的二进制形式，结果为字符串,nbits表示返回的二进制位数
    """
    lis = []
    while True:
        num,rem = divmod(num,2)
        lis.append(rem)
        if num == 0:
            break
    while len(lis) < nbits:
        lis.append(0)		# 保证输出为32位的二进制
    return ''.join([str(x) for x in lis[::-1]]) # -1为逆序

def bin_hex(bin_str):
    """将二进制字符串转化为16进制字符串
    """
    hex_str = hex(int(bin_str, 2))[2:]
    hex_str = hex_str.strip('L')

    while len(hex_str) < 8:
        hex_str = '0' + hex_str

    return hex_str
    
def circle_left_shift(string, x):
	"""circle shift the string x bits left
	"""
        return string[x:] + string[0:x]

def round_fun(B, C, D, round):
	"""每轮函数
	"""
        B = int(B, 2)
        C = int(C, 2)
        D = int(D, 2)
        if round == 0:
            res = (B & C) | (~B & D)
        elif round == 1 or round == 3:
            res = B ^ C ^ D
        elif round == 2:
            res = (B & C) | (B & D) | (C & D)

        return dec_bin(res, 32)

def mod32add(*binary):            # 可变参数
	"""进行模2^32加
	"""
        two = []
        for element in binary:
            two.append(int(element, 2))

        return dec_bin((sum(two)) % 2**32, 32)


if __name__ == '__main__':
	print dec_bin(int('01001001001000000110110001101111',2), 32)
        print int('01001001001000000110110001101111',2) ^ 2223333333
        print bin_hex('00000000000000000000000000001111')
