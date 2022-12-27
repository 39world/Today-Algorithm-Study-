# 알고리즘 공부 #01
# 백준 2869
import math
A,B,V = map(int, input().split());

if V-A <= 0 :
    day = 1
else :
    day = math.ceil((V-A)/(A-B)) + 1;

print(day);
