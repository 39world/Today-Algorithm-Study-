# 알고리즘 공부 #01
# 백준 1110
print('0보다 크거나 같고 99보다 작은 자연수 A값을 입력해주세요');
a = int(input());
a_target = a;
b = 0;
number=0;
while (1) :
    b = a//10 + a%10;
    a = (a%10)*10+ b%10;
    number += 1    
    if (a == a_target):
        break
print(number);
print('종료되었습니다.');