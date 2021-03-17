# 알고리즘 공부 #02
# 백준 1010

import sys
input = sys.stdin.readline


test_case = int(input());

stack = [];

while test_case != 0:   
    test_case -= 1
    commend = input().split();
    if commend[0] == 'push':
        stack.append(commend[1])
        continue
    if commend[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        continue
    if commend[0] == 'size':
        print(len(stack))
        continue
    if commend[0] == 'empty':
        if len(stack) == 0 :
            print(1)
            continue
        else : 
            print(0)
            continue
    if commend[0] == 'pop':
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack[-1])
        stack.pop()
        continue