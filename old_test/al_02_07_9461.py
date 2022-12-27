# 알고리즘 공부 #02
# 백준 9461


import sys


def now_tri(n):
    global tri_line
    if n <= 3 :
        line = 1;
        return line
    elif 3 < n <=5:
        line = 2;
        return line;
    if tri_line[n] :
        return tri_line[n]
    line = now_tri(n-1) + now_tri(n-5)    
    tri_line[n] = line
    return line

test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())
    tri_line = [0]*(n+1)
    result = now_tri(n);
    print(result)



