T = int(input())

for test_case in range(1, T + 1):
    
    day = int(input())
    priceList = list(map(int, input().split()))
    answer = [0]*day
    
    maxPrice = priceList[-1]
    for i in range(day-2,-1,-1):
        if maxPrice > priceList[i]:
            answer[i+1] = maxPrice-priceList[i] #왜 i+1인지 아직 해결 못함. i일때 런타임에러가 발생했음 ㅜㅜ 
        else:
            maxPrice = priceList[i]
    
    print(f"#{test_case}",sum(answer))

## 우와 삼성 코테 어렵다.. 