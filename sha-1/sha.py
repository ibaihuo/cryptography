#!/usr/bin/env python
#-*- coding:utf-8 -*-
import grouped
import base

K = ['5a827999',
     '6ed9eba1',
     '8f1bbcdc',
     'ca62c1d6']

for i in range(4):
    K[i] = base.hex_bin(K[i])

def sha1(message):
    """
    """
    groups = grouped.grouped_pad(message) # 获得消息的二进制分组
    #print groups
    for group in groups:
        H = ['67452301','efcdab89','98badcfe','10325476','c3d2e1f0']
        for i in range(5):
            H[i] = base.hex_bin(H[i])
        #print H[i]

        words = grouped.expand(group)   # 将每组消息扩展为80个字
        #print words
        FIVE = H
        (A, B, C, D, E) = (FIVE[0], FIVE[1], FIVE[2], FIVE[3], FIVE[4])
        #print FIVE
        for step in range(80):
            round = step / 20           # 4轮循环
            aA = base.circle_left_shift(A, 5) # 左移5位
            BCD = base.round_fun(B, C, D, round)
            #print 'aA = %s, BCD = %s' % (aA, BCD)
            tmp = base.mod32add(aA, BCD, E, words[step], K[round])
            
            aB = base.circle_left_shift(B, 30)
            (A, B, C, D, E) = (tmp, A, aB, C, D)
            FIVE = [A, B, C, D, E]
            #print 'FIVE:', FIVE
            print 'step %d :' % step,
            for i in range(5):
                haha = base.bin_hex(FIVE[i])
                print haha,
            print
        for i in range(5):
            H[i] = base.mod32add(H[i], FIVE[i])
        print 'The groups answer:', 
        for h in H:
            print base.bin_hex(h),
        print
    
    result = []
    for i in range(5):
        result.append(base.bin_hex(H[i]))
    return ''.join(result)

if __name__ == '__main__':
    message = 'goodforme'
    print sha1(message)
