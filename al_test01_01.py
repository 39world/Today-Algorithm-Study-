# 알고리즘 공부 #01 Test
# 백준 1920

import sys

have_cdnum = sys.stdin.readline()
have_cards = set(sys.stdin.readline().split())
want_cdnum = int(sys.stdin.readline())
want_cards = list(sys.stdin.readline().split())

for i in want_cards :        
    if i in have_cards:       
        print(1, end = ' ')
    else:          
        print(0, end = ' ')   
          