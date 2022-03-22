##프로그래머스 키패드 누르기
def solution(numbers, hand):
    answer = ''
    leftSide = [1,4,7]
    rightSide = [3,6,9]
    numberPad = {};
    
    x,y = 0,0
    for num in range(1,10):
        numberPad[num] = [x,y]
        if num%3 == 0:
            x += 1
            y = 0
        else :
            y += 1
    numberPad[0] = [3,1]
    
    leftHand = [3,0]
    rightHand = [3,2]
    for i in numbers:
        if i in leftSide:
            answer += 'L'
            leftHand = numberPad[i]
        elif i in rightSide:
            answer += 'R'
            rightHand = numberPad[i]
        else : 
            rightD = abs(rightHand[0]-numberPad[i][0])+abs(rightHand[1]-numberPad[i][1])
            leftD = abs(leftHand[0]-numberPad[i][0])+abs(leftHand[1]-numberPad[i][1])
            if rightD < leftD :
                answer += 'R'
                rightHand = numberPad[i]
            elif rightD > leftD:
                answer += 'L'
                leftHand = numberPad[i]
            if rightD == leftD and hand == 'right':
                answer += 'R'
                rightHand = numberPad[i]
            elif rightD == leftD and hand == 'left' :
                answer += 'L'
                leftHand = numberPad[i]
    
    return answer