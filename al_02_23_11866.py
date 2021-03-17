# 알고리즘 공부 #02
# 백준 11866

import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())

if n == 1 :
    print('<%d>' %(n))
    exit()
q= deque()
stack = []

for i in range(1,n+1):
    q.append(i);

while q:
    
    for i in range(k-1):
        q.append(q[0]);
        q.popleft()
    stack.append(q[0])
    q.popleft()

for i in range(n):
    if i == 0 :
        print('<%d,' % (stack[0]), end=' ')
        continue
    elif i == n-1:
        print ('%d>' %(stack[-1]))
    else :
        print ('%d,' %(stack[i]), end=' ')

