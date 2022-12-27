# 알고리즘 공부 #01
# 백준 10250

test_case = int(input());
while test_case != 0:    
    height, width, person = map(int, input().split());
    if person%height > 0 :
        hotel_flo = str(person%height);
    else :
        hotel_flo = str(height);    
    hotel_ho = person//height + 1;
    if hotel_ho < 10 :
       hotel_ho = '0'+str(hotel_ho); 
    else :
        hotel_ho = str(hotel_ho) ;   
    print(hotel_flo+hotel_ho);    
    test_case -= 1;

