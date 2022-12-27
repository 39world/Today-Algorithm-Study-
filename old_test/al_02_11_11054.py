# 알고리즘 공부 #02
# 백준 11054

import sys
input = sys.stdin.readline

length = int(input())

num_list = list(map(int, input().split()))

result = [0]*length;
up = [0]*length;
down = [0]*length;

for i in range(length):
    for j in range(0,i):
        if num_list[i] > num_list[j] and up[i] <= up[j] :
            up[i] = up[j] +1;

for i in range(length-1,0,-1):
    for j in range(length-1,i,-1):
        if num_list[i] > num_list[j] and down[i] <= down[j]:
            down[i] = down[j] +1
for i in range(length):
    result[i] = up[i] + down[i] +1

print(max(result))