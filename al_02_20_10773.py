# 알고리즘 공부 #02
# 백준 10773

import sys
input = sys.stdin.readline


test_case = int(input())
stack=[]
result = 0;

while test_case != 0 :
    test_case -= 1;

    a = int(input());

    if a == 0 :
        stack.pop();
    else :
      stack.append(a);

for i in range(len(stack)):
    result += stack[i]
print(result)