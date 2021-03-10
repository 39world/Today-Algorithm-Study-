# 알고리즘 공부 #01
# 백준 2606

import sys
from collections import deque

def line_up():
    global com_lined
    while temp_q :
        x,y = temp_q.popleft();    
        if y not in com_lined[x]:
            com_lined[x].append(y);
        if x not in com_lined[y]:
            com_lined[y].append(x);
    return

def virus(start_com):
    global com_lined
    global com_status
    for i in com_lined[start_com]:
        if com_status[i] == 0:
            com_status[i] = 1;
            virus(i)
        else:
            continue
    return
com_num = int(sys.stdin.readline());
line_num = int(sys.stdin.readline());

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(line_num)];
com_lined = [list() for _ in range(0,com_num+1)];
com_status = [0]*(com_num+1)
cnt = 0;
temp_q = deque(lines)
start_com = 1;
com_status[1] = 1;

line_up();

virus(1);

for i in com_status:
    if i == 1:
        cnt += 1
print(cnt-1);
