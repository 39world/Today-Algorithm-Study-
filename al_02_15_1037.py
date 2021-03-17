# 알고리즘 공부 #02
# 백준 1541

import sys
input = sys.stdin.readline


num_case = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

print(num_list[0]*num_list[-1])