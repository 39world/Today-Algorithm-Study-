# 알고리즘 공부 #02
# 백준 11866

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def line_up(lined):
    while lined:
        a,b = lined.popleft()
        if b not in line_status[a] :  
            line_status[a].append(b);
        if a not in line_status[b]:
            line_status[b].append(a);
    return 


def find_DFS(starting):
    result.append(starting);
    for i in line_status[starting]:
        if status[i] == 0:
            status[i] = 1;
            find_DFS(i)
        else :
            continue
    return 

def find_BFS(starting):    
    result.append(starting);
    for i in line_status[starting]:
        if status[i] == 0:
            status[i] = 1;            
            q.append(i);
    while q :
        a = q.popleft()
        find_BFS(a)
    return



n,m,v = map(int, input().split())

status = [0]*(n+1);

lined = [list(map(int,input().split())) for _ in range(m)]

line_status = [list() for _ in range(0,n+1)]
stack = []
q = deque()
lined = deque(lined)
result = []

status[v] = 1;
line_up(lined);
for i in line_status:
    i.sort()

find_DFS(v)

for i in range(len(result)):
    if i == len(result)-1:
        print(result[i]);
    else :
     print(result[i], end=(' '));
result = [];
status = [0]*(n+1);
status[v] = 1;

find_BFS(v)
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i]);
    else :
     print(result[i], end=(' '));