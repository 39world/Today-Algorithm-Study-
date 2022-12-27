def solution(n):
    answer = 0
    sqrt_num = n**(1/2);
    temp_num = round(sqrt_num);
    if sqrt_num == temp_num :
        answer = (sqrt_num+1)**2;
    else :
        answer = -1
    return answer