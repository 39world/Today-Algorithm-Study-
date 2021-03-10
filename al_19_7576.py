# 알고리즘 공부 #01
# 백준 7576
import sys 
from collections import deque



def find_start(t_width,t_height,lines):
    global temp_q
    for i in range(0,t_height):
        for j in range(0,t_width):
            if lines[i][j] == 1:                
                start= [i,j];
                temp_q.append(start);    
    return


def go_tomato():        
    while temp_q:
        x,y = temp_q.popleft()         
        for i in range(4):
            next_x = x + x_move[i];                
            next_y = y + y_move[i];
               
            if 0<= next_x < t_height and 0<= next_y < t_width :
                if lines[next_x][next_y] == 0 :
                    lines[next_x][next_y] = lines[x][y] +1;
                    temp_q.append([next_x,next_y])
    return                     
       
x_move = [0,0,-1,1]
y_move = [-1,1,0,0]

t_width,t_height = map(int, sys.stdin.readline().split());

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(t_height)];
start = []
temp_q = deque()
find_start(t_width,t_height,lines);
if temp_q == False :
    print(0)
else : 
    go_tomato() 
    day = max(map(max,lines)) -1 
    for i in range(0,t_height):
        for j in range(0,t_width):
            if lines[i][j] == 0:
                print(-1)
                exit()
    print(day)


# print(go_tomato(start[0],start[1]));