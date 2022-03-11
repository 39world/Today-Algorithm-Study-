#프로그래머스 완주하지 못한 선수

#처음 문제를 보고 떠올린 코드는 
#들어온 순서대로 참가 목록을 지워서 남은 한 명을 찾아내려고 했다.
#completion의 길이는 participant의 길이보다 1 작습니다. 라는 조건을 참고.

def solution(participant, completion):   
      
    for i in participant :
        participant.remove(i);
    answer = participant[0]          
    
    return answer

#하지만 이렇게하면 효율성 검증에서 모두 실패했다.
#for문을 돌려 계속해서 찾아내기때문에 n*n의 복잡도가 되어버렸다.

#이를 개선하기 위해서 복잡도를 줄이는 방법을 생각해봤다.

def solution(participant, completion):   
      
    partDict = {}
    compleDict = {}
    for i in participant :
        if i not in partDict :
            partDict[i] = 1
        else :
            partDict[i] = partDict[i]+1
    
    for i in completion :
        if i not in compleDict :
            compleDict[i] = 1
        else :
            compleDict[i] = compleDict[i]+1
        
    
    for i in partDict.keys():
        if i not in compleDict or partDict[i] != compleDict[i] :
            return i
#이처럼 for문을 통해 디렉토리를 만들고, 비교한다면 n+n+1, 복잡도가 n이 되어 효율성에서 통과했다.

import collections

def solution(participant, completion):   
    
    partDict = collections.Counter(participant)
    compleDict = collections.Counter(completion)
    for i in partDict.keys():
        if i not in compleDict or partDict[i] != compleDict[i] :
            return i

#이처럼 collections의 Counter를 이용하면 코드를 줄일 수 있다! 