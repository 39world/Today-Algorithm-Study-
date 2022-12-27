# 알고리즘 공부 #02
# 백준 2108

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

numavg = sum(numbers);



print(round(numavg/n));

print(numbers[n//2])


nums_dict = Counter(numbers) 
nums_most = nums_dict.most_common()
if len(numbers) > 1 : 
    if nums_most[0][1] == nums_most[1][1]: 
        print(nums_most[1][0])
    else : 
        print(nums_most[0][0])
else : 
    print(nums_most[0][0]) 
   

print(numbers[-1]-numbers[0])