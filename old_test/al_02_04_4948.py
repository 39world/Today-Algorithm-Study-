# 알고리즘 공부 #02
# 백준 4948

import sys


sosu_max = 246912;
status = [True]*(sosu_max+1);
status[1] = False;
for i in range(2,sosu_max+1):
    if status[i] != False:
        for j in range(i+i,sosu_max,i) :
            status[j] = False;
while 1 :    
    cnt = 0;
    n = int(sys.stdin.readline());
    min_num = n ;
    max_num = n*2;
    if n==0:
        exit()
    for i in range(min_num,max_num+1):
        if status[i] == True:
            cnt += 1;
    print(cnt);        
