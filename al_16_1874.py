# 알고리즘 공부 #01
# 백준 1874



import sys

max_num = int(sys.stdin.readline())
count = 1 ;
stack = [];
result = [];
no_result = True;

for i in range(max_num) :
    target_num = int(sys.stdin.readline());
    while count <= target_num :
        stack.append(count);
        result.append('+');
        count += 1;
    if stack[-1] == target_num:
        stack.pop();
        result.append('-');
    else :
        no_result = False;     
        
if no_result == False:
    print('No');
else :
    for i in result :
        print(i);