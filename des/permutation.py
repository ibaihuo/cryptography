#!/usr/bin/env python
#-*- coding:utf-8 -*-
######################################################################
## Filename:      permutation.py
##                
## Copyright (C) 2009,  renewjoy
## Version:       0.1
## Author:        renewjoy <rlj_linux@126.com>
## Created at:    Sun Mar  1 11:16:04 2009
##                
## Description:   perform some permutation
##                
######################################################################

import table
import binary

# permutation the original binary code using the permutation_table
# return a str that permuted
def permutation(original, permutation_table):
	"""To permutation the binary code with the permutation_table table
	"""
	permuted = []
	row = len(permutation_table)	# get the table's rows
	colum = len(permutation_table[0]) # get the table's colum
	for i in range(0, row):
		for j in range(0, colum):
			index = permutation_table[i][j] - 1
			permuted.append(original[index])

	if __name__ == '__main__':
		print 'The permutation table is:'
		for i in range(0, row):
			for j in range(0, colum):
				print permutation_table[i][j],
			print		# just for a newline	

	return ''.join(permuted)	# return a str

def s_box(original):
	"""permutation with the S box
	"""
	B = [original[:6],
	     original[6:12],
	     original[12:18],
	     original[18:24],
	     original[24:30],
	     original[30:36],
	     original[36:42],
	     original[42:48]
	     ]
	#print 'B =', B

	new_B = []
	for i in range(1, 9):
		M_row = int(B[i-1][0] + B[i-1][5], 2)
		N_colum = int(B[i-1][1:5],2)
		#print 'M_row = :', M_row
		#print 'N_colum = :', N_colum

# 		sub_box = 'table.substitution_box_%s' % str(i)
# 		print 'sub_box:', (sub_box)
		if i == 1:
			sub_box = table.substitution_box_1
		elif i == 2:
			sub_box = table.substitution_box_2
		elif i == 3:
			sub_box = table.substitution_box_3
		elif i == 4:
			sub_box = table.substitution_box_4
		elif i == 5:
			sub_box = table.substitution_box_5
		elif i == 6:
			sub_box = table.substitution_box_6
		elif i == 7:
			sub_box = table.substitution_box_7
		elif i == 8:
			sub_box = table.substitution_box_8

		#print sub_box[M_row][N_colum]

		#print 'This is:', B[i-1]
		temp = binary.hexstr_binary(hex(sub_box[M_row][N_colum])[-1])
		new_B.append(temp)
		#print temp
	new_B = ''.join(new_B)
	#print 'new_B = ', new_B

	return new_B

if __name__ == '__main__':
	import table		 # permutation table
	import string		 # for constant letters
	import binary		 # to solve some format to binary code
	
	key_string = string.letters + string.digits + '#@' # This is only for testing, so to use the letters
	print 'key_string is:', key_string
	print 'The len of key_string is:', len(key_string)

	permuted_string = permutation(key_string, table.permuted_choice_1)
	print 'permuted_string is:', ''.join(permuted_string)
	print 'The len of permuted_string is:', len(permuted_string)

	test = '100101001001011100110011100101001000101100001111' # 48 bits
	print s_box(test)
	print 'The len is:', len(s_box(test)) # 32 bits
