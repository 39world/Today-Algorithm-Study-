# 알고리즘 공부 #02
# 백준 2609

import sys
input = sys.stdin.readline


n, k = map(int, input().split())

up = 1;
down =1;

for i in range(1,n+1):
    up = up*i;

for j in range(1,k+1):
    down = down * j

for k in range(1,n-k+1):
    down = down*k

print(up//down)