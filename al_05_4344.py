# 알고리즘 공부 #01
# 백준 4344
case_number = int(input());
start_number = 0;
test_grade = [list(map(int, input().split())) for _ in range(case_number)]

while case_number != start_number :   
    student_number = test_grade[start_number][0];    
    count = int (0);
    sum_grade = sum(test_grade[start_number][1:]);    
    av_grade = sum_grade/test_grade[start_number][0];    
    for i in test_grade[start_number][1:] :
        if i > av_grade :
            count += 1 ;
    rate =(count/student_number)*100;     
    print('%.3f'%rate+'%');
    start_number += 1;

# # 알고리즘 공부 #01
# # 백준 4344
# print('테스트 케이스의 개수를 입력해주세요 !');
# case_number = int(input());

# while case_number != 0 :
#     print('%d번의 테스트가 남았습니다. 학생의 수와 학생 점수를 적어주세요 ex) 5 50 50 70 80 100' %(case_number));
#     test_grade = list(map(int, input().split()));
#     student_number = test_grade[0];
#     count = int (0);
#     sum_grade = sum(test_grade[1:]);
#     av_grade = sum_grade/test_grade[0];
#     for i in test_grade[1:] :
#         if i > av_grade :
#             count += 1 ;
#     rate =(count/student_number)*100;     
#     print('%.3f'%rate);
#     case_number -= 1;
# print('종료되었습니다.');


