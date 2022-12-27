# 알고리즘 공부 #02
# 백준 11399

import sys
input = sys.stdin.readline


people = int(input())

people_time = list(map(int, input().split()))

now_time = 0;
total_time = 0;

people_time.sort()

for i in people_time:
    now_time += i;
    total_time += now_time;

print(total_time)
    