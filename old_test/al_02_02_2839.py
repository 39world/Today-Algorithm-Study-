# 알고리즘 공부 #02
# 백준 2839

import sys 

max_sugar = int(sys.stdin.readline());
cnt = 0;
while max_sugar >= 0:        
    if max_sugar % 5 == 0 :
        cnt += max_sugar //5;
        print(cnt)
        exit()
    else :
        cnt += 1;
        max_sugar -= 3;
print(-1)        
            
