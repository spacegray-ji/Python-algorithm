"""
file_name: 5585.py
author: Geonwoo Ji
environment: python 3.11.4

Baekjoon, Q-5585, 거스름돈
"""

import sys

n = int(sys.stdin.readline())

coins = [500, 100, 50, 10]
ret_list = []

for i in coins:
    ret_list.append(n//i)
    n = n % i

print(ret_list)
