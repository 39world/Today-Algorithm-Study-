# 알고리즘 공부 #02
# 백준 2798


import sys

input = sys.stdin.readline

n,m = map(int, input().split())


card_list = list(map(int, input().split()))

card_list.sort(reverse = True)

def find_num(x):
    max_num = 0;
    for i in range(len(card_list)):
        for j in range(i+1,len(card_list)):
            for k in range(j+1,len(card_list)):
                result = card_list[i]+card_list[j]+card_list[k]   
                if max_num > result:      
                    continue
                elif result <= m and max_num < result:
                    max_num = result
                
    print(max_num)
    return


find_num(0)