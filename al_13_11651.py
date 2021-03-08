# 알고리즘 공부 #01
# 백준 11651


case_number = int(input());
start_number = 0;
location = [list(map(int, input().split())) for _ in range(case_number)]
location.sort(key = lambda x : (x[1],x[0]));
for i in location :
    print(i[0],i[1]);