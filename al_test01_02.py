# 알고리즘 공부 #01 Test
# 백준 2164

import sys 
from collections import deque

card_number = int(sys.stdin.readline())
card_set = []
for i in range(1,card_number+1):
    card_set.append(i)

que_card = deque(card_set);

while True :    
    if len(que_card) == 1 :
        print(que_card[0]);
        break
    else:
        que_card.popleft();
        que_card.append(que_card[0]);
        que_card.popleft()