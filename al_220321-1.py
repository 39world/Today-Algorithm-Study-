#프로그래머스 오픈채팅방

def solution(record):
    answer = []
    idList = {}
    printer = {'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}
    for log in record:
        splitLog = log.split(' ')
        if splitLog[0] in ['Enter','Change']:
            idList[splitLog[1]] = splitLog[2]
    
    for log in record:
        splitLog = log.split(' ')
        if splitLog[0] in ['Enter','Leave']:
            answer.append(idList[splitLog[1]]+printer[splitLog[0]])
    return answer


##startswith 라는 함수가 있다.
#맨 앞에 오는게 무엇인지 판단하는 함수.
#이를 이용하면 

def solution(record):
    answer = []
    printer = {'Enter':'님이 들어왔습니다.','Leave':'님이 나갔습니다.'}
    idList = {}
    for log in record:        
        if log.startswith('Enter') or log.startswith('Change'):
            splitLog = log.split(' ')
            idList[splitLog[1]] = splitLog[2]
    
    for log in record:
        if log.startswith('Enter') or log.startswith('Leave'):
            splitLog = log.split(' ')
            answer.append(idList[splitLog[1]]+printer[splitLog[0]])
    return answer