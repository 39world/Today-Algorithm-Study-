n,m = map(int, input().split())
temp_map = [[0]*m for _ in range(n)];

x,y,direction = map(int,input().split());

temp_map[x][y] = 1;

game_map = [];
for i in range(n):
    game_map.append(list(map(int,input().split())));

dx = [-1,0,1,0];
dy = [0,1,0,-1];

def turn_left():
    global direction;

    direction -= 1;
    if direction == -1 :
        direction = 3;

count = 1
turn_time = 0;
while True:
    turn_left();
    nx = x+dx[direction];
    ny = y + dy[direction];
    if temp_map[nx][ny] == 0 and game_map[nx][ny] ==0 :
        temp_map[nx][ny] = 1;
        x = nx;
        y = ny;
        count += 1;
        turn_time = 0;
    else:
        turn_time += 1        
    
    if turn_time == 4:
        nx = x - dx[direction];
        ny = y - dy[direction];

        if game_map[nx][ny] == 0:
            x = nx;
            y = ny;
        else: 
            break
        turn_time = 0;
print(count);
            





