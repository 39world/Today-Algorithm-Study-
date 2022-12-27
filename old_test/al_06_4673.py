# 알고리즘 공부 #01
# 백준 4673
print('10,000보다 작거나 셀프 넘버는 다음과 같습니다.');
# a = 0;
# c = 0;
# while a<= 10000 :
#     b = 0;
#     a += 1;
#     while b<a :
#         c = b + b%10 + b//10%10 + b//100%10 + b//1000%10 + b//10000%10;
#         b += 1;
#         if c == a :
#             break
#         if b == a : 
#             print(a);
A = set(range(1,10001))
B = set();
for i in A :
    for j in str(i):
        i += int(j);
    B.add(i);
C = sorted(A-B);
for i in C :
    print(i);
print('종료되었습니다.');