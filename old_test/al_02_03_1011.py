# 알고리즘 공부 #02
# 백준 2839

import sys 

test_case = int(sys.stdin.readline())
result = [];
for i in range(test_case):
    start_point,final_point = map(int, sys.stdin.readline().split());
    distance = final_point-start_point;
    cnt=0;
    k=0;
    while 1 :
        k += 1;
        if distance - k*k <=0 :
            print(1)
            cnt = k;
            break
        elif 0 < distance - k*k and distance - k*k <= k:
            print(2)
            cnt = 2*k ;
            break
        elif k < distance - k*k and distance - k*k <= 2*k:
            print(3)
            cnt = 2*k+1;
            break
        print('한바퀴')   
    result.append(cnt)
for i in result:
    print(i)    