def solution(a, b):
    answer = 0
    if a>b : 
        cnt = b;
        max = a;
    else :
        cnt = a;
        max = b;
        
    while cnt <= max :
        answer = answer + cnt;
        cnt += 1;
    
    return answer