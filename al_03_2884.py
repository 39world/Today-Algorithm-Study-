# 알고리즘 공부 #01
# 백준 2884
print('내일 일어나야 하는 시간은 몇시 몇분인가요? EX) 10 20 → 10시 20분');
a,b = map(int, input().split());

if (b>=45):
    b = b-45;
    print(a, b);

else :
    a = a-1;
    b = 60-(45-b);
    if a<0 :
        a = 24+a;
        print(a,b);
    else:
     print(a,b);
print('종료되었습니다.');