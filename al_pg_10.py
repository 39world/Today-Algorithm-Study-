def solution(brown, yellow):
    
    
    a = brown+yellow  #x*y
    
    b = (brown+4)//2 #x+y
    
    for i in range(1,2000001):
        x = a//i 
        if a%i == 0 and x+i == b:
            answer=[x,i]
            return answer

solution(10,2)