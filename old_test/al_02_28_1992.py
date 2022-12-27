# 알고리즘 공부 #02
# 백준 1992


import sys

input = sys.stdin.readline

n = int(input());

video_input = [list(input()) for _ in range(n)]


video = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        video[i][j] = int(video_input[i][j])


def find_video(x,y,cnt):
    now_video = video[x][y]
    for i in range(x,x+cnt):
        for j in range(y,y+cnt):
            if video[i][j] != now_video :
                print('(', end='');
                find_video(x,y,cnt//2);
                find_video(x,y+cnt//2,cnt//2)
                find_video(x+cnt//2,y,cnt//2);
                find_video(x+cnt//2,y+cnt//2,cnt//2);
                print(')', end='')
                return
    if now_video ==1:
        print(1,end='');
        return
    else:
        print(0, end='');
        return


find_video(0,0,n);