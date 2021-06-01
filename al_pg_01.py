# 알고리즘 공부 심화
# 프로그래머스 주식

import sys

input = sys.stdin.readline

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    temp_array = deque();
    for i in range(len(progresses)):            
       temp_array.append(math.ceil((100 - progresses[i])/speeds[i]));
    while 0 < len(temp_array):        
        cnt = 1;        
        if len(temp_array)==1:
            answer.append(1);
            break
        for i in range(1,len(temp_array)):
            if temp_array[0]>= temp_array[i]:
                cnt +=1;
            elif temp_array[0]<temp_array[i]:
                break        
        answer.append(cnt);
        print(answer)
        while cnt != 0:
            temp_array.popleft();
            cnt -=1;                              
    
    return answer

a = [93,30,55];
b = [1,30,5]
print(solution(a,b))    