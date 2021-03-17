# 알고리즘 공부 #02
# 백준 18258

import sys
from collections import deque
input = sys.stdin.readline



def order_give():
        
    order = list((input().split()))

    if order[0] == 'push' :
        que.append(order[1])
        return
    elif order[0] == 'front':
        if not que:
            print(-1)
            return
        else :
            print(que[0])
            return
    elif order[0] == 'back':
        if not que:
            print(-1)
            return
        else :
            print(que[-1])
            return
    elif order[0] == 'size':
        print(len(que))
        return
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
            return
        else :
            print(0)
            return
    elif order[0] == 'pop':
        if not que:
            print(-1)
            return
        else :
            print(que[0])
            que.popleft()
            return
    
    return




test_case = int(input());
que = deque()
for i in range(test_case):
    order_give()
