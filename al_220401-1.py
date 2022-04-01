## 프로그래머스 소수 만들기
## 매우 간단한 문제! 

from itertools import combinations

def solution(nums):
    answer = 0
    
    era = [True] * 3000  #에라토스테네스의 체를 이용해서 소수인지 아닌지 판별
    limitNum = int(3000**0.5)
    for i in range(2,limitNum):
        if era[i] :
            for j in range(i*2, 3000, i):
                era[j] = False
                
    comList = list(combinations(nums,3))    
    
    for arr in comList:
        if era[sum(arr)]:       
            answer += 1            
    
    return answer

## combinations 를 이용해서 3개로 이루어진 쌍 리스트를 만드는게 핵심! 