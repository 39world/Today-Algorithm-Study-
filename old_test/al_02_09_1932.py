# 알고리즘 공부 #02
# 백준 1932


import sys

n = int(sys.stdin.readline())

numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0;

sum_list = [[0]*n for _ in range(n)]
temp_left = []
temp_right = []
sum_list[0][0] = numbers[0][0]
m=2;
for i in range(1,n):
    for j in range(m):
        if j==0 :
            sum_list[i][j] = numbers[i][j] + sum_list[i-1][0];
        elif j==i :
            sum_list[i][j] = numbers[i][j] + sum_list[i-1][j-1]
        else :
            temp_left = numbers[i][j] + sum_list[i-1][j-1];
            temp_right = numbers[i][j] + sum_list[i-1][j];
            sum_list[i][j] = max(temp_left,temp_right);
    m += 1
print(max(sum_list[n-1]))
