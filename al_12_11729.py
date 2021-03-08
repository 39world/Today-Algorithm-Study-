# 알고리즘 공부 #01
# 백준 11729
import sys

def hanoi (n,start,temp,target):
    if n == 1 :
        print(start,target);
        
    else :
        hanoi (n-1,start,target,temp);
        print(start,target);        
        hanoi (n-1,temp,start,target);
    

n = int(sys.stdin.readline())
print(2**n-1);
hanoi(n,1,2,3);