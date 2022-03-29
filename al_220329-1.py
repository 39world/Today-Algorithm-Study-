## 프로그래머스 음양 더하기

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i] :
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    
    return answer