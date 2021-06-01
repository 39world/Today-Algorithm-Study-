s = "one4seveneight"
import math
def solution(s):
    answer = []
    temp_1 = 0;
    i = 0;
    while i < len(s):
        if s[i].isdigit():
            answer.append(int(s[i]))
            i +=1;
        else :
            if s[i] == 'z':
                answer.append(0);
                i +=4;
            elif s[i] == 'o':
                answer.append(1);
                i +=3;
            elif s[i] ==  't':
                if s[i+2] == 'o':
                    answer.append(2);
                    i += 3;
                else :
                    answer.append(3);
                    i += 5;
            elif s[i] == 'f':
                if s[i+3] == 'r':
                    answer.append(4);
                    i +=4;
                else : 
                    answer.append(5);
                    i += 4;
            elif s[i] == 's':
                if s[i+2] == 'x':
                    answer.append(6);
                    i +=3;
                else : 
                    answer.append(7);
                    i += 5;
            elif s[i] == 'e':
                answer.append(8);
                i +=5;
            else : 
                answer.append(9);
                i +=4;   
    longnum = len(answer);   
    j=0;
    while j < longnum:
       temp_1 += answer[j] * math.pow(10,(longnum-j-1));
       j+=1;   
       print(j)
        
    return int(temp_1)

print(solution(s));

print(math.pow(10,(2)))