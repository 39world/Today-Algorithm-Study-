# 알고리즘 공부 #02
# 백준 1992


import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(1,n+1):
    arr.append(i);

comb = combinations(arr,m)

print(comb)

for i in comb:
    for j in range(m):
        print(i[j])

# for i in cb :
#     for j in range(m) :
#         if j != m - 1:
#             print(i[j], end = ' ')
#         else :
#             print(i[j], sep= '\n')
