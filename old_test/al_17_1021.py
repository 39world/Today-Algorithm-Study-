# 알고리즘 공부 #01
# 백준 1021

import sys
import math

num_size, want_size = map(int, sys.stdin.readline().split());
#처음에는 큐의 크기와 뽑아내려고 하는 수의 개수를 받아줍니다.
want_list = list(map(int, sys.stdin.readline().split()));
#뽑아내려고 하는 수의 위치를 입력받아 리스트로 만들어주세요
num_list = []
cnt = 0;
#우리가 사용하기위해 큐의 크기만큼 만들어줄 리스트와 이동 횟수를 저장할 변수를 초기화해주세요
#이제 1부터 입력받은 큐의 크기만큼 리스트로 만들어줍니다
for i in range(1,num_size+1) :
    num_list.append(i);
#두번째로 입력받았던 뽑아내려는 수의 위치를 앞에서 부터 하나하나 돌아가며 for문으로 찾아냅니다
for i in want_list :
    if num_list.index(i)+1 <= math.ceil(len(num_list)/2) : 
        #index를 이용해서 뽑아내려고 하는 수의 위치를 큐 속에서 찾아내고 0부터 시작하기에 1을 더해줬습니다.
        #그리고 현재 큐의 길이를 2로 나눠서 이보다 작거나 같으면 앞으로 가져도록
        #크면 뒤로 빼도록 나눠줍니다. 
        while True :
            #앞으로 이동시키는게 빠를때, 맨 앞의 수가 우리가 찾는 수라면
            #그 수를 리스트에서 지우고 다음 수를 찾기위해 종료
            if num_list[0] == i :  
                del num_list[0];                 
                break
            else :
                #맨 앞의 수가 우리가 찾는 수가 아니라면 
                #맨 앞의 수를 맨 뒤에 추가해주고
                #맨 앞의 수를 삭제합니다, 이동했으니 카운트에 +1하고 계속 진행
                num_list.append(num_list[0]);
                del num_list[0];                
                cnt +=1;
    else :
        while True:
            #뒤로 이동시키는게 빠를때, 맨 뒤의 수가 우리가 찾는 수라면
            #그 수를 리스트에서 지우고 다음 수를 찾기위해 종료. 
            #이때 지민이가 가지고 있는 큐는 앞으로 빼는 기능밖에 없기때문에
            #맨 뒤를 앞으로 보내주고 삭제해야합니다.
            #이 과정을 생략했으니 카운트에 +1을 해줍니다.
            if num_list[-1] == i :
                del num_list[-1];
                cnt += 1;               
                break
            else :
                #맨 뒤의 수가 우리가 찾는 수가 아니라면
                #그 수를 insert를 통해서 맨 첫번째에 끼워넣어주고
                #마지막 수를 지워줍니다.
                #앞으로 보내줬으니 카운트 +1
                num_list.insert(0,num_list[-1]);
                del num_list[-1];              
                cnt += 1;
#for문이 돌면서 우리가 원하던 수를 다 찾았으니 cnt에 적힌 숫자를 출력
print(cnt);
