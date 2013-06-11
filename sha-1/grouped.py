#!/usr/bin/env python
#-*- coding:utf-8 -*-

import base, binascii

def grouped_pad(string):
	"""对字符串进行填充，然后按512bit进行分组
	返回分组的结果
	"""
	string = binascii.b2a_hex(string) # 转化为16进制
	bin = base.hex_bin(string)	  # 转化为二进制
	#print bin
	#print len(bin)
	length_pad = base.dec_bin(len(bin), 64) # 最后填充的消息本身长度
	#print length_pad
	mod = len(bin) % 512
	#print mod
	if mod == 0:
		bin += '1'		# 填1位'1'
		bin += '0' * 511	# 填511位'0'
		bin += length_pad
	#最好的bits数小于448 
	else:
		bin += '1'		# 填1位'1'
		bin += '0' * (447-mod)	# 填448 - 1 - mod位'0'
		bin += length_pad	# 填充信息的二进制长度

	grouped = []
	i = 0
	while i+512 <= len(bin):
		grouped.append(bin[i:i+512])
		i += 512
	return grouped

def expand(group):
	"""将每个512分组再进行分组，并扩展到80个小分组
	"""
	words = []
	for i in range(0, 512, 32):
		words.append(group[i:i+32])
	#print words
	for i in range(16, 80):
		temp = int(words[i-3],2) ^ int(words[i-8],2) ^ int(words[i-14], 2) ^ int(words[i-16], 2) # 异或
		temp = base.dec_bin(temp, 32)	       # 获得二进制
		temp = base.circle_left_shift(temp, 1) # 循环左移一位
		words.append(temp)
	#print len(words)
	return words

if __name__ == '__main__':
	print grouped_pad('abc')
	print expand(grouped_pad('abc')[0])
