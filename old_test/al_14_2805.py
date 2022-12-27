# 알고리즘 공부 #01
# 백준 2850
import sys
import math


def find_height(all_tree,tree,want_tree) :
    
    start_cut = 1;
    max_cut = max(tree);
    mid = ((start_cut + max_cut)//2);
    while True :   
        holding = 0  
        print(mid)
        for i in tree :
            if i<=mid :
                #print('pass')
                continue
            else :
                #print('cut')
                holding += i-mid;        
                #print(holding)  
        if holding < want_tree :
            if want_tree-holding >= mid :
                #print('작은데 다시')
                mid = ((mid+1)//2)
            else :
                #print('작은데 1차이')
                mid -= 1;            
        elif holding == want_tree:
            #print('딱맞음')
            break
        else : 
            #print('크니까 다시')
            mid = ((mid+max_cut)//2)
                
    return mid
   

#나무의 수, 원하는 나무의 양
all_tree, want_tree = map(int, sys.stdin.readline().split());
#주어진 나무의 길이
tree = list(map(int, sys.stdin.readline().split()));

print(find_height(all_tree,tree,want_tree));