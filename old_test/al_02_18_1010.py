# 알고리즘 공부 #02
# 백준 1010

import sys
input = sys.stdin.readline


test_case = int(input())



while test_case != 0:
    test_case -= 1;
    temp_a, temp_b = 1,1
    a, b = map(int, input().split())
    
    for i in range(1,b+1):
        temp_b = temp_b * i
    for j in range(1,a+1):
        temp_a = temp_a * j

    for k in range(1,b-a+1):
        temp_a = temp_a * k
    print(temp_b//temp_a)