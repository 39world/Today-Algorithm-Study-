# 알고리즘 공부 #02
# 백준 1149

import sys

house_num = int(sys.stdin.readline())

house = [list(map(int, sys.stdin.readline().split())) for i in range(house_num)]


money_result = [[0]*3 for _ in range(house_num)]
for i in range(3):
    money_result[0][i] = house[0][i];
if house_num >1 :
    for j in range(1,house_num):
        before_r,before_g,before_b = money_result[j-1]
        now_r = min(before_g,before_b)+house[j][0]
        now_g = min(before_r,before_b)+house[j][1]
        now_b = min(before_r,before_g)+house[j][2]
        
        money_result[j][0] = now_r
        money_result[j][1] = now_g
        money_result[j][2] = now_b
result= min(money_result[house_num-1][0],money_result[house_num-1][1],money_result[house_num-1][2])
print(result)

