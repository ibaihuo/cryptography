#!/usr/bin/env python
#-*- coding:utf-8 -*-
######################################################################
## Filename:      binary.py
##                
## Copyright (C) 2009,  renewjoy
## Version:       0.1
## Author:        renewjoy <rlj_linux@126.com>
## Created at:    Sun Mar  1 11:19:00 2009
##                
## Description:   some binary code processing
##                
######################################################################

#import binascii

# convert a hex-string to it's binary code
# return the binary code
# retury type: str
def hexstr_binary(hex_str):
	"""convert hex-str to it's binary code
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

def circle_shift_left(string, x):
	"""circle shift the string x bits left
	"""
	if x == 1:
		return string[1:] + string[0]
	elif x == 2:
		return string[2:] + string[:2]

def format(binary_code, bits = 8, seperate_char = ' '):
	"""Turn the binary_code to a new format, every bits grouped, with a `seperate_char` char between groups
	"""
	new_format = []
	for i in range(0, len(binary_code), bits):
		new_format.append(binary_code[i:i+bits])
	return seperate_char.join(new_format)	# seperated with the character `seperate_char` which default space

# xor bit by bit with two binary code strings
def xor_bybit(first, second):
	"""To xor the binary code string bit by bit
	"""
	bit_xor = []
	for i in range(0, len(first)):
		bit_xor.append(str((int(first[i], 2) ^ int(second[i], 2))))
	return ''.join(bit_xor)

if __name__ == '__main__':
	key = '0123456789abcdef'
	key_binary = hexstr_binary(key)
	print key_binary
	print format(key_binary)
	print format(key_binary, 8, '\n')
	first =  '01010110011110001001101010111100110111101111000000010010'
	second = '11110000110011001010101000001010101011001100111100000000'
	print xor_bybit(first, second)
