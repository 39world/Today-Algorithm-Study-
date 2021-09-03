def solution(dirs):
    answer = 0
    location = [4,4];
    game_map = [[[0,0,0,0] for _ in range(10)] for _ in range(10)];
    direction = 0;
    for i in dirs:
        if i == 'U' and location[1] != 9:
            location[1] += 1;
            if game_map[location[0]][location[1]][0] == 0:
                game_map[location[0]][location[1]][0] = 1;
                game_map[location[0]][location[1]-1][1] = 1;
                answer += 1;
        elif i == 'D' and location[1] != 0:
            location[1] -= 1;     
            if game_map[location[0]][location[1]][1] == 0:
                game_map[location[0]][location[1]][1] = 1;
                game_map[location[0]][location[1]+1][0] = 1;
                answer += 1;  
        elif i == 'R' and location[0] != 9:
            location[0] += 1;
            if game_map[location[0]][location[1]][2] == 0:
                game_map[location[0]][location[1]][2] = 1;
                game_map[location[0]-1][location[1]][3] = 1;
                answer += 1;  
        elif i == 'L' and location[0] != 0:
            location[0] -= 1;
            if game_map[location[0]][location[1]][3] == 0:
                game_map[location[0]][location[1]][3] = 1;
                game_map[location[0]+1][location[1]][2] = 1;
                answer += 1;              
            
    return answer