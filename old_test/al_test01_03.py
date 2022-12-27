# 알고리즘 공부 #01 Test
# 백준 2751

import sys 

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]
    return merge(merge_sort(left_list),merge_sort(right_list))

def merge(list1,list2):
    result = []
    list1_index = 0;
    list2_index = 0;
    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] < list2[list2_index]:
            result.append(list1[list1_index])
            list1_index +=1;
        else :
            result.append(list2[list2_index])
            list2_index +=1;

    if list1_index == len(list1):
        while list2_index < len(list2):
            result.append(list2[list2_index]);
            list2_index +=1;

    if list2_index == len(list2):
        while list1_index < len(list1):
            result.append(list1[list1_index]);
            list1_index +=1;
    return result


case = int(sys.stdin.readline())
num_list = []
while case != 0:
    case -= 1;
    new_num = int(sys.stdin.readline())
    num_list.append(new_num)   
result_list = merge_sort(num_list)   
for i in result_list:
    print(i)

