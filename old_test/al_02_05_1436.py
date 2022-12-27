# 알고리즘 공부 #02
# 백준 1436

import sys

n = int(sys.stdin.readline());
start = 666;
cnt=0;
while 1:
    if '666' in str(start):
        cnt += 1;
    if cnt == n :
        break    
    start +=1    
print(start)

