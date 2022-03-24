##프로그래머스 없는 숫자 더하기
## 첫 답
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
            
    return answer

#간단하게 줄이면

def solution(numbers):
    
    return sum(i for i in range(10) if i not in numbers)

#numbers의 모든 원소는 서로 다르다는 조건이 있으므로
#45에서 numbers의 원소를 더해서 빼는 방법도 있다.

def solution(numbers):
    return 45- sum(numbers)