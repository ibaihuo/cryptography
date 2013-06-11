#!/usr/bin/env python
#-*- coding:utf-8 -*-
######################################################################
## Filename:      des.py
##                
## Copyright (C) 2009,  renewjoy
## Version:       0.1
## Author:        renewjoy <rlj_linux@126.com>
## Created at:    Sun Mar  1 11:41:02 2009
##                
## Description:   To encrypt a 8-hex-string or 8-characters with the DES encryption
##                
######################################################################

import binascii

# modules table, binary, permutation is created by myself
import table				# import the DES tables
import binary				# to solve some format to binary code
import permutation			# to perform some permutation

def des(plaintext_hexstr, key_hexstr, mode = 'encrypt'):
	"""Encrypt a plaintext_bin with the key_bin, Or Decrypt a cipher_bin with the key_bin
	"""
	plaintext_bin = binary.hexstr_binary(plaintext_hexstr) # get the string's 64bits binary code
	key_bin = binary.hexstr_binary(key_hexstr) # get the string's 64bits binary code
	#############################################################
	#############################################################
	# To get the turn_key 1-16
	#############################################################
	#############################################################
	# permuted choice 1
	after_permuted_choice_1 = permutation.permutation(key_bin, table.permuted_choice_1)
	#print 'After permuted choice 1 is:', binary.format(after_permuted_choice_1)
	#print 'The len of after_permuted_choice_1 is', len(after_permuted_choice_1)

	C_0 = after_permuted_choice_1[:28]
	D_0 = after_permuted_choice_1[28:]
	#print 'C_0 is: ', binary.format(C_0, 7)
	#print 'D_0 is: ', binary.format(D_0, 7)

	C_1 = C_0
	D_1 = D_0

	turn_key = []
	# get the turn_key by turn 16 times
	for times in range(16):
		# circle shift left 1 or 2 bit(s)
		C_1 = binary.circle_shift_left(C_1, table.shift_table[times])
		D_1 = binary.circle_shift_left(D_1, table.shift_table[times])

		#print 'C_1 shift left', table.shift_table[times], 'bits is: ', C_1
		#print 'D_1 shift left', table.shift_table[times], 'bits is: ', D_1

		after_permuted_choice_2 = permutation.permutation(C_1+D_1, table.permuted_choice_2) # permuted choice 2

		turn_key.append(after_permuted_choice_2)
		#print 'The turn_key[', times + 1, '] is:', binary.format(after_permuted_choice_2, 6)
		#print 'The len of after_permuted_choice_2 is:', len(after_permuted_choice_2)

	#print 'The turn key is:', turn_key
	#print len(turn_key)

	# #####################################################
	# #####################################################
	# Encrypt the Data
	# #####################################################
	# #####################################################

	# Do the initial permutation
	after_init_perm = permutation.permutation(plaintext_bin, table.initial_permutation)
	#print 'After initial permutation is:', binary.format(after_init_perm)

	L_0 = after_init_perm[:32]
	R_0 = after_init_perm[32:]
	#print 'The L_0 is:', binary.format(L_0)
	#print 'The R_0 is:', binary.format(R_0)


	R_1 = R_0

	# judging is the mode
	if mode == 'encrypt':
		range_type = range(16)
	elif mode == 'decrypt':
		range_type = range(15, -1, -1)

	# do the 16 tiems turn
	for i in range_type:
		temp = R_1
		#print 'Round:', i+1

		# Expansion R_1 from 32bits to 48bits, using the expansion table
		E = permutation.permutation(R_1, table.expansion) # now, E is 48bits
		#print 'E :', binary.format(E, 6)
		#print 'KS :', binary.format(turn_key[i], 6)

		# Xor E with turn_key[i]
		R_xor_turnkey = binary.xor_bybit(E, turn_key[i])
		#print 'E xor KS:', binary.format(R_xor_turnkey, 6)

		# S box permutation
		s_box = permutation.s_box(R_xor_turnkey)
		#print 'Sbox:', binary.format(s_box, 4)

		# P permutation
		P = permutation.permutation(s_box, table.permutation_p)
		#print 'P :', binary.format(P)

		# Xor P with L_0
		R_1 = binary.xor_bybit(L_0, P)

		L_0 = temp			# L[i] = R[i+1]
		#print 'The L[',i+1, ']:', binary.format(L_0)
		#print 'The R[',i+1,']:', binary.format(R_1)
		#print

	final = R_1 + L_0			# exchange the left 32bits with right 32bits
	#print 'R[16]L[16]:', binary.format(final)

	# do the inverse initial permutation
	output = permutation.permutation(final, table.inverse_initial_permutation)
	#print 'Output:', binary.format(output)

	# Turn binary code to hexdecimal
	output_hex = []
	for i in range(0, 64, 4):
		#print output[i:i+4]
		output_hex.append(hex(int(output[i:i+4],2))[-1])
	if mode == 'encrypt':
		#print 'The encryped hexdecimal is:', ''.join(output_hex)
		return ''.join(output_hex)
	else:
		#print 'The decrypted hexdecimal is:', ''.join(output_hex)
		#decrypt_text = binascii.a2b_hex(''.join(output_hex))
		#print 'The decrypted text is:', decrypt_text
		#return decrypt_text
		return ''.join(output_hex)

def main():
	"""The main for test
	"""
	# This for user input 8 characters.
	# plain_text = raw_input ('please input 8 characters for plain text:')
	# key = raw_input ('please input 8 characters for key:')
	# if plain_text != 8 or key != 8:
	# 	#print '8 characters only allowed.'
	# 	exit
	# plain_text = binascii.b2a_hex(plain_text) # get the hexdecimal format
	# key = binascii.b2a_hex(key)		  # get the hexdecimal format

	#plain_text = 'AB831A095638991F'
	#plain_text = plain_text.lower()

	#key = 'ABCDEFGH'
	key = 'BBBBBBBB'
	key = binascii.b2a_hex(key)		# get the hexdecimal format
	print key
	#plain_text = '37ba569b7dafc7d7'
	plain_text = '2fe108be39835d20'
	#plaintext_bin = binary.hexstr_binary(plain_text)
	#print 'plaintext_binary is:', binary.format(plaintext_bin)
	#print 'The len of plaintext_bin is:', len(plaintext_bin)

	#print 'key_binary is:', binary.format(key_bin)
	#print 'The len of key_binary is:', len(key_bin)
	print binascii.a2b_hex(des(plain_text, key, 'decrypt')) # encrypt 

if __name__ == '__main__':
	main()
