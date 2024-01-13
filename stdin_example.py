"""
file_name: stdin_example.py
author: Geonwoo Ji
environment: python 3.11.4
"""


import sys


# 한 개의 값을 입력받을 때
a = sys.stdin.readline()
print('input var:', a, type(a), 'length:', len(a))


# 한 개의 정수를 입력받을 때
a = int(sys.stdin.readline())
print('input var:', a, type(a), 'length:', len(a))


# 정해진 개수의 정수를 한 줄에 입력받을 때
a, b, c = map(int, sys.stdin.readline().split())
print('input var:', a, type(a), 'length:', len(a))
print('input var:', b, type(b), 'length:', len(b))
print('input var:', c, type(c), 'length:', len(c))


# 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때
data = list(map(int, sys.stdin.readline().split()))
print('input var:', data, type(data), 'length:', len(data))


# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
data = []
n = int(sys.stdin.readline())

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

print('input var:', data, type(data), 'length:', len(data))


# 문자열 n줄을 입력받아 리스트에 저장할 때
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
print('input var:', data, type(data), 'length:', len(data))
