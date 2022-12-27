# 알고리즘 공부 #02
# 백준 2579


import sys

num_stairs = int(sys.stdin.readline())


score = [int(sys.stdin.readline()) for _ in range(num_stairs)]


max_score = [0]*num_stairs;

max_score[0] = score[0]
if num_stairs > 1:
    max_score[1] = score[0]+score[1]
if num_stairs >2:
    max_score[2] = max(score[0]+score[2],score[1]+score[2])

for i in range(3,num_stairs):    
    max_score[i] = max((max_score[i-3]+score[i-1]+score[i]),(max_score[i-2]+score[i]))

print(max_score[num_stairs-1])



# import sys

# num_stairs = int(sys.stdin.readline())
# score = []
# max_score = []
# for _ in range(num_stairs):
#     score.append(int(sys.stdin.readline()))

# max_score.append(score[0])
# max_score.append(score[0]+score[1])
# max_score.append(max(score[0]+score[2],score[1]+score[2]))

# for i in range(3,num_stairs):
#     max_score.append( max((max_score[i-3]+max_score[i-1]+score[i]),(max_score[i-2]+score[i])))
# print(max_score[num_stairs-1])