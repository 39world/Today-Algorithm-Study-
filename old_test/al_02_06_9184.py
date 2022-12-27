# 알고리즘 공부 #02
# 백준 9184

import sys

result = [[[-1]*21 for _ in range(21)] for _ in range(21)]

# for i in range(0,21):
#     for j in range(0,21):
#         for k in range(0,21):
#             result[i][j][k] = -1;

def w(a,b,c):
    
    if a <=0 or b <= 0 or c <= 0:
        return 1
    elif a>20 or b >20 or c >20:
        return w(20,20,20)
    elif result[a][b][c] != -1 :
        return result[a][b][c]   
    elif a<b and b<c :
        now_data = (w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)); 
        result[a][b][c] = now_data
        return now_data
    else :
        now_data = (w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1));
        result[a][b][c] = now_data
        return now_data

while 1 :
    a,b,c = map(int, sys.stdin.readline().split())
    if a == -1 and b ==-1 and c ==-1 :
        break 
    temp_result = w(a,b,c)
    print('w(%d, %d, %d) = %d' %(a,b,c,temp_result))
