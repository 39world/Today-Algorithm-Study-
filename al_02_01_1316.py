# 알고리즘 공부 #02
# 백준 1316


import sys 

test_case = int(sys.stdin.readline()) #케이스 숫자 입력 
#케이스 숫자 만큼 문자열을 받기
test_str = [list(sys.stdin.readline().strip()) for _ in range(test_case)] 

cnt= 0;
for i in range(test_case): #케이스 숫자만큼 돌아가며 입력 받은 문자열 판단
    temp_1=[]
    temp_str = set(test_str[i]); #중복된 문자열을 제거    
    for j in range(len(test_str[i])):        
        if j == len(test_str[i])-1:
            temp_1.append(test_str[i][j])            
            break
        else :
            if test_str[i][j] == test_str[i][j+1] :                
                continue
            else :                 
                temp_1.append(test_str[i][j])    
    if len(temp_1) == len(temp_str):
        cnt += 1
print(cnt)
        
