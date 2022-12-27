# 알고리즘 공부 #01
# 백준 2941
# print('단어를 입력해주세요!');
# word = input();
# cro_1 = 'c='
# cro_2 = 'c-'
# cro_3 = 'dz='
# cro_4 = 'd-'
# cro_5 = 'lj'
# cro_6 = 'nj'
# cro_7 = 's='
# cro_8 = 'z='
# i=int(1);
# cro_num=int(0);
# while true:
#     cro_num =+ word.count(cro)


# cro_num = word.count(cro_1)+word.count(cro_2)+word.count(cro_3)+word.count(cro_4) + word.count(cro_5)+word.count(cro_6)+word.count(cro_7)+word.count(cro_8);
# print('크로아티아 알파벳은 %d개 입니다.'%cro_num);

print('단어를 입력해주세요!');
word = input();
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_num=0;
total_cro =0;
for i in cro :
    cro_num = word.count(i)    
    if cro_num != 0 :
        total_cro += cro_num;
        word = word.replace(i,'a');
print('크로아티아 알파벳 %d개를 포함해 총 알파벳은 %d개입니다. 입니다.'%(total_cro,len(word)));