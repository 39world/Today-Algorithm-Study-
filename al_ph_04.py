#프로그래머스 다음 큰 숫자 문제 

def solution(n):
    count = bin(n).count('1');
    for m in range(n+1,1000001):
        if(bin(m).count('1') == count):
            return m