# 알고리즘 공부 #01
# 백준 1929
import sys

num_min, num_max = map(int,sys.stdin.readline().split());
pan = [True]*(num_max+1);
for i in range(2,num_max+1) :
    if pan[i] ==True:
        for j in range(i+i,num_max+1,i):
            pan[j]= False;
for i in range(num_min,num_max+1):
     if pan[i] == True:
         print(i)
  
         