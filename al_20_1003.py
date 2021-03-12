# 알고리즘 공부 #01
# 백준 1003

import sys

fibo_data = [0]*41
fibo_zerone = [0]*41

def fibo_find(n, fibo_data):
    global fibo_zerone
    if fibo_data[n] != 0:
        return fibo_data[n]

    elif n == 0 :
        fibo_zerone[n] =[1,0]
        fibo_data[n] = 0;
        return fibo_data[0]

    elif n == 1:
        fibo_zerone[n] = [0,1]
        fibo_data[n] = 1;
        return fibo_data[1]

    now_fibo = fibo_find(n - 1, fibo_data) + fibo_find(n - 2, fibo_data)
    now_zero= fibo_zerone[n-1][0]+fibo_zerone[n-2][0]
    now_one = fibo_zerone[n-1][1]+fibo_zerone[n-2][1]
    fibo_zerone[n] = [now_zero,now_one]
    fibo_data[n] = now_fibo
    return now_fibo

test_case = int(sys.stdin.readline());
while test_case != 0:    
    n = int(sys.stdin.readline());     
    fibo_find(n,fibo_data);   
    print("%d %d" % (fibo_zerone[n][0], fibo_zerone[n][1]))
    test_case -=1;     


