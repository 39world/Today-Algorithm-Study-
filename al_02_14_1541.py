# 알고리즘 공부 #02
# 백준 1541

import sys

input = sys.stdin.readline


a = input().split('-');
total = []
for i in a:
    sum = 0;
    b=i.split('+')
    for j in b:
        sum += int(j)
    total.append(sum)
result = total[0]
for i in range(1,len(total)):
    result -= total[i]
print(result)


