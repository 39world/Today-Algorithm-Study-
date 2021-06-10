#프로그래머스 폰켓몬

def solution(nums):
    temp_n = set(nums);
    n = len(nums)//2;
    
    if n > len(temp_n):
        answer = len(temp_n);
    else :
        answer = n;
    
    return answer