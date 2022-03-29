## 프로그래머스 내적

def solution(a, b):
    answer = sum(a*b for a,b in zip(a,b))    
    return answer