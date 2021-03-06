# 알고리즘 공부 #01
# 백준 2588
print('세 자리 자연수 A, B를 입력해주세요 ! ex) 472 385');
a,b = map(int, input().split());
b_1 = b%10;
b_10 = (b//10)%10;
b_100 = b//100;
ab_1 = a* b_1;
ab_10 = a* b_10;
ab_100 = a* b_100;
print(ab_1);
print(ab_10);
print(ab_100);
print(ab_1+(10*ab_10)+(100*ab_100));
print('종료되었습니다.');