# 알고리즘 공부 #02
# 백준 2667

import sys
from collections import deque

input = sys.stdin.readline

x_move = [0,0,-1,1]
y_move = [1,-1,0,0]
def find_house(x,y):
    global cnt
    global house_map
    for i in range(4):
        if 0<= x+x_move[i] < height and 0<= y+y_move[i] < len(house_map[0]):       
            if int(house_map[x+x_move[i]][y+y_move[i]]) == 1 :
                house_map[x+x_move[i]][y+y_move[i]] = 0;
                cnt += 1;
                find_house(x+x_move[i],y+y_move[i])
    return


height = int(input());


house_map = [list(input().strip()) for _ in range(height)]
result = []
for i in range(height):
    for j in range(len(house_map[0])):
        if int(house_map[i][j]) == 1:
            house_map[i][j] =0 ;
            cnt = 1
            find_house(i,j);
            result.append(cnt)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])           