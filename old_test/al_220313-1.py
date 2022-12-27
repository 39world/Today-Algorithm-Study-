# 프로그래머스 문자열 압축

# 전체 길이의 절반을 넘어가면 절대 압축할 수 없기에 s의 길이 절반만큼만
# 간격으로 잡게끔 len(s)//2 + 1을 최대로 range를 돌려줬다.
# 마지막 글자는 cnt가 올라가고 바로 끝나버려서 
# 압축 시키도록 두번째 for문 끝에 cnt가 있다면 압축한 글자수를 측정하도록 만들었다.
# 테스트 케이스를 모두 통과했지만 제출하면 계속 실패하는 케이스들이 존재했다.
# 이를 해결하기 위해서 계속 고민했는데
# 처음에는 압축 후 압축된 문자의 숫자가 무엇이던 1을 빼주도록 코딩했었던게 문제였다.
# 10을 넘어가거나 100을 넘어가면 1이아니라 2, 3을 빼줘야 하는데, 이를 놓쳤다.
# 그래서 len(str(s))를 이용해서 압축된 갯수만큼 전체 글자수에서 빼도록 고쳐줬다.
def solution(s):
    answer = len(s)
    for x in range(1, len(s)//2+1) :        
        cnt = 1
        word = ''
        tempWord = ''
        tempAnswer = len(s)
        for i in range(0, len(s), x) :
            tempWord = s[i:i+x]
            if word == tempWord :
                cnt += 1
            else :
                if cnt != 1:
                    tempAnswer -= len(word)*(cnt-1) - len(str(cnt))
                word = tempWord
                cnt = 1
        if cnt != 1:
            tempAnswer -= len(word)*(cnt-1) -len(str(cnt))
        answer = min(answer,tempAnswer)
    return answer