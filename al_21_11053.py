# 알고리즘 공부 #01
# 백준 11053

import sys

def find_group(size_num,numbers):
    global cnt    
    for i in range(size_num) :                            
        for j in range(i):                 
            if numbers[j] < numbers[i] and cnt[i] <= cnt[j] :
               cnt[i] = cnt[j]+1;              
    return

size_num = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = [1]*size_num;
max_cnt = 0;
find_group(size_num,numbers)
print(max(cnt))
