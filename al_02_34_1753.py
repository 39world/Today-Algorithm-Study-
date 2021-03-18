# 알고리즘 공부 #02
# 백준 1753

import sys

input = sys.stdin.readline

v , e = map(int, input().split())

start = int(input())

line = [[0] for _ in range(v+1)]
value = [[0 for _ in range(v+1)] for _ in range(v+1)]


max_value = [0 for _ in range(v+1)]

def line_up(u,v,w):
    value[u][v] = w ;
    line[u].append(v);    

    return

def touch(start):
    for i in line[start]:
        if i == 0 :
            continue
        if max_value[i]==0 or max_value[i] > max_value[start] + value[start][i]:
            max_value[i] = max_value[start] + value[start][i]
            touch(i)
    return

while e != 0:
    e -= 1;
    u,v,w = map(int, input().split())
    line_up(u,v,w)
    
touch(start);

for i in range(1,len(max_value)):
    if i == start :
        print(0);
    elif max_value[i] == 0 :
        print('INF')
    else : 
        print(max_value[i])
        



    
