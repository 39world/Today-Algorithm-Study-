#프로그래머스 타겟 넘버

def solution(numbers, target):
    answer = 0
    lastidx = len(numbers)
    def dfs(idx,result):
        if idx == lastidx:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1,result+numbers[idx])
            dfs(idx+1,result-numbers[idx])
                
    dfs(0,0)      
    
    return answer