places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from collections import deque

x_move = [0,0,1,1,1,-1,-1,-1]
y_move = [1,1,1,0,-1,1,0,-1]
temp_q = deque()
result=[];

def solution(places):
    
    answer = []
    for k in range(0,5):
        for i in range(0,5):
            for j in range(0,5):
                if places[k][i][j] == 'P':
                    people = [k,i,j];
                    temp_q.append(people);  
    cnt = 0;
    exK = 0;
    while temp_q:
        k,x,y = temp_q.popleft();
        if exK < k :
            result.append(cnt);
            exK +=1;
            cnt = 0;        

        for i in range(8):
            next_x = x + x_move[i];
            next_y = y + y_move[i];
            
            if 0<= next_x <5 and 0<= next_y < 5:              
                
                if places[k][next_x][next_y] == 'P' :
                    if places[k][x][next_y] == 'X' and places[k][next_x][y] == 'X':
                        cnt +=1               
                        
    result.append(cnt);   
    for i in result:
        if i != 0:
            answer.append(0);
        else :
            answer.append(1);                       
    print(answer)
    return answer

solution(places)