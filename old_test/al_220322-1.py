#프로그래머스 숫자 문자열과 영단어

def solution(s):
    s = s.replace('zero','0')
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five','5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    answer = int(s)
    return answer

# 딕셔너리와 for를 사용해 중복된 코드 제거

def solution(s):
    numList = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for num in numList.items():
        s = s.replace(num[0],num[1])
    answer = int(s)
    return answer