# 알고리즘 공부 #02 test
# 백준 1920

import sys

input = sys.stdin.readline


n = int(input())

n_list = list(map(int, input().split()))


m = int(input())

m_list = list(map(int, input().split()))

n_list.sort()

def finding(list, target,first,last):
    if first > last :
        print(0)
        return

    mid = (first + last) //2

    if list[mid] == target :
        print(1)
        return

    elif list[mid] > target :         
        finding(list,target,first,mid-1)
    elif list[mid] < target:        
        finding(list,target,mid+1,last)


last = len(n_list)-1

for i in m_list:
    finding(n_list,i,0,last)