#프로그래머스 위장

def solution(clothes):
    closet = {};
    for val, key in clothes :
        if key in closet :
            closet[key].append(val);
        else :
            closet[key] = [val];
    answer = 1;
    for key in closet.keys():
        answer *= len(closet[key])+1
    return answer-1