# 알고리즘 공부 #02
# 백준 2609

import sys
input = sys.stdin.readline


a, b = map(int, input().split())

temp_a, temp_b = a,b;

while temp_b != 0:
    temp_a = temp_a %temp_b
    temp_a, temp_b = temp_b, temp_a

mini = temp_a ;

maxi = a*b // mini 

print(mini)
print(maxi)