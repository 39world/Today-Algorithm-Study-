# 알고리즘 공부 #01
# 백준 1157
# print('영어 단어를 입력해주세요 ! ');
# word_input = input().upper();
# count= int()
# count_max = int(0)
# word = int()
# target = int()
# count_word=[];

# for i in word_input :
#     count = word_input.count(i);
#     if count > count_max : 
#         count_max = count;
#         word = i;
#         target = i;
#     elif count == count_max :
#         if target != word :
#             target = '?';
#         else :
#             target = i;
# print(target);
# print('종료되었습니다.');


print('영어 단어를 입력해주세요 ! ');
word_input = input().upper();
print(word_input)
deleted_word = list(set(word_input));
print(deleted_word)
cnt_number = []
count_max = int(0)
target = int()


for i in deleted_word :
    cnt_number.append(word_input.count(i));   
count_max = max(cnt_number); 
maxcount = cnt_number.count(count_max);
if maxcount > 1 :
    print('?');
else :
    target = cnt_number.index(count_max);
    print(deleted_word[target]);

print('종료되었습니다.');

    

   
