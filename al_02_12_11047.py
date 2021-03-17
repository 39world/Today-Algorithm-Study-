# 알고리즘 공부 #02
# 백준 11047


import sys
input = sys.stdin.readline

test_case, target = map(int, input().split());

coin_list = [int(input()) for _ in range(test_case)]

coin_list.sort(reverse=True);

now_coin = 0;
cnt =0;
for i in coin_list:
    cnt += target //i
    target = target % i
    if target == 0:
        break

print(cnt)