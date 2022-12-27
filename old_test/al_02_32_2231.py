# 알고리즘 공부 #02
# 백준 2231

import sys

input = sys.stdin.readline

n = int(input())
num = 1;
while True : 
    num += 1
    num_list = str(num)
    one = 0

    for i in num_list:
        one += int(i) ;

    if (one + num) == n:
        print(num)
        break