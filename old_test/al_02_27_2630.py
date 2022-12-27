# 알고리즘 공부 #02
# 백준 2630

# import sys

# input = sys.stdin.readline


n = int(input());

paper = [list(map(int, input().split())) for _ in range(n)]

white , blue = 0, 0;

def cut(x,y,cnt):
    global white, blue
    now_color = paper[x][y]
    for i in range(x,x+cnt):
        for j in range(y,y+cnt):
            if now_color != paper[i][j]:
                cut(x,y,cnt//2)
                cut(x,y+cnt//2,cnt//2)
                cut(x+cnt//2,y,cnt//2)
                cut(x+cnt//2,y+cnt//2,cnt//2)
                return
    if now_color == 0 :
        white += 1;
        return
    else :
        blue += 1
        return
cut(0,0,n)
print(white)
print(blue)        

