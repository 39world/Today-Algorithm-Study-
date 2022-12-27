# 알고리즘 공부 #02
# 백준 2231
import sys
import math
n = int(sys.stdin.readline().split()[0])
arr =[]
for _ in range(n) :
    x1, y1, r1, x2, y2, r2 = list(map(int, (sys.stdin.readline().split())))
    d = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    maxR = 0
    if r1 < r2 :
        temp = r1
        r1 = r2
        r2 = temp
    
    if d == 0 and r1 != r2 :
        arr.append(0)
    elif d == 0 and r1 == r2 :
        arr.append(-1)
    elif r1 + r2 == d  :
        arr.append(1)
    elif r1 - r2 < d and d < r1 + r2: 
        arr.append(2)
    elif abs(r1 - r2) == d :
        arr.append(1)
    elif r1 + r2 < d:
        arr.append(0)
    elif abs(r1 - r2) > d:
        arr.append(0)

for i in arr :
    print(i)

