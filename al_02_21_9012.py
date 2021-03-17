# 알고리즘 공부 #02
# 백준 9012

import sys
input = sys.stdin.readline


test_case = int(input())


while test_case != 0:
    test_case -= 1
    stack = []
    cnt = 0;
    data = input();

    for i in data :
        if i == '(' :
            stack.append(i)
        elif i == ')':
            if not stack :
                print('NO')
                cnt = 1
                break
            else:                
                stack.pop();
    if cnt == 0 :
        if not stack :
            print('YES')
        else :
            print('NO')
