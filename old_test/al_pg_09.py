#프로그래머스 2 x n 타일링 

def solution(n):
    array = [0]*(n+1)
    
    array[1] = 1;
    array[2] = 2;
    
    for i in range(3,n+1):
        array[i] = (array[i-1] + array[i-2])%1000000007
        
    
    answer = array[n]
    return answer