# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a program to solve Tower of Hanoi
"""

cnt = 0
def Move(k,fr,to,other):
    global cnt
    cnt += 1
    if k == 1:
        print(k,':',fr,' -> ',to)
        return
    else :
        Move(k-1,fr,other,to)
        print(k,':',fr,' -> ',to)
        Move(k-1,other,to,fr)

Move(4,'a','b','c')
print("in total:",cnt)