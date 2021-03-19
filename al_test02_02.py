# 알고리즘 공부 #02 test
# 백준 1920

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

n_list = []
status = [False]*n
result = []


for i in range(1,n+1):
    n_list.append(i)


def line_up(i):

    if i == m :
        for k in result:
            if k == result[-1]:
                print(k, sep= '\n')
                return
            else :
                print(k, end=' ')
    for j in range(len(n_list)):
        if not status[j]:
            status[j] = True
            result.append(n_list[j])
            line_up(i+1)
            status[j] = False
            result.pop()

line_up(0)


