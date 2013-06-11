#!/usr/bin/env python
#-*- coding:utf-8 -*-

def miller_rabin(a, n):
    rem = []
    p = n -1
    while p:
        rem.append(p & 1)                   # get the last bit
        p >>= 1                             # shift right one bit
#    print rem
    rem.reverse()                           # resverse the list
    print rem

    d = 1
    for bit in rem:
        print 'bit =', bit,
        x = d
        d = d**2 % n
        if d == 1 and x != 1 and x != n-1:
            return True
        if bit == 1:
            d = d*a % n
            if d != 1:
                return True
        print a, d, x,
    return False

if __name__ == '__main__':
    print miller_rabin(2, 21)
    print miller_rabin(3, 322222222222222222222222222222222222222222222222222222222222222222222222222222222289111111111111111191833333333333333333333333333333333312)
#     for i in range(2, 100):
#         print miller_rabin(2, i)
