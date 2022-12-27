#프로그래머스 신규 아이디 추천
# 처음에는 정규식을 떠올렸으나 if와 while만 사용해도 깔끔할 것 같았다.
#파이썬은 정말 문자열 다루기에 너무 편리하다

def solution(new_id):
    #1단계 소문자 치환
    new_id = new_id.lower()
    #2단계 문자 제거
    answer = ''
    for i in new_id:
        if i.isalnum() or i in '-_.' :
            answer += i
    #3단계 마침표 치환
    while '..' in answer :
        answer = answer.replace('..','.')
    #4단계 처음과 끝 마침표 제거
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    #5단계 빈 문자열 체크
    if answer == '':
        answer = 'a'
    #6단계 16자 이상 체크
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1] 
    #7단계 길이 조절
    while len(answer) < 3:
        answer += answer[-1]
    return answer