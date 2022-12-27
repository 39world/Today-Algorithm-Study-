## 생각보다 기존 시험 대행 프로세스와 다르다
## 구현 자체만 신경쓰는 것이 아니라 메모리 할당도 신경써야 하는게 포인트인듯 .

T = int(input())
 
for test_case in range(1, T + 1):
    numList = map(int,input().split())
    answer = 0
    for num in numList:
        if num%2 == 0:
            continue
        else:
            answer += num
    case = '#'+str(test_case)
    print(case,answer)