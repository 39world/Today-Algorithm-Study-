# 알고리즘 공부 #01
# 백준 4949

import sys

while True:
    word = sys.stdin.readline()
    stack = []
    word_result = 1;
    before_word = 0;
    for now in word :
        if now == '(' or now == '[' :
            stack.append(now)
        elif now == ')':
            if  not stack or stack[-1]=='[' :
                word_result = 0;
                before_word = 1;
                break
            elif stack[-1]=='(':           
                stack.pop();
                
        elif now ==']':
            if not stack or stack[-1]=='(':
                word_result = 0; 
                before_word = 1;
                break            
            elif stack[-1]=='[':            
                stack.pop();
                
        elif now == '.':
            break       
    if before_word == False and word_result ==True :     
        print('yes');
    else :
        print('no');

