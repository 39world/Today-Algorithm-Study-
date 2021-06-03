# 알고리즘 공부 #02 test
# 백준 1920

import sys
input = sys.stdin.readline


n = int(input())

result = [0]*(n+1);

def sum(num):
    print(num)
    if num == 1 :
        result[1] = 1;
        return 1
    if num == 2:
        result[2] = 2;
        return 2
    if result[num] != 0:
        return result[num]
    else : 
        result[num] = sum(num-1) + sum(num-2)
        return result[num]

last = sum(n)
print(last%15746)




# zero_max = n//2;

# result = 0;

# for i in range(zero_max+1):
#     num = n-i;
#     temp_up = 1;
#     temp_down = 1;
#     if i == 0 :
#         result += 1;
#         continue
#     if i*2 == n:
#         result += 1;
#         continue
#     for j in range(1,num+1):
#         temp_up = temp_up * j;
#     for k in range(1, num-i+1):
#         temp_down = temp_down * k;
#     result += (temp_up // temp_down);

# print(result%15746)

