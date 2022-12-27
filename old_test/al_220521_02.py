# 프로그래머스 짝지어 제거하기
def solution(s):
    
    stack = []
    
    for i in s:
        
        if len(stack) == 0:
            stack.append(i)
            continue
            
        if i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
                
    if len(stack) >0:
        return 0
    else:
        return 1