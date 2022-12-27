#프로그래머스 프린터

import java.util.*;

class Solution {
    
    class Work {
    int location;
    int prior;
    
    public Work(int location, int prior){
        this.location = location;
        this.prior = prior;
        }
    }
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Work> que = new LinkedList<>();
        
        for(int i = 0; i<priorities.length;i++){
            que.add(new Work(i,priorities[i]));
        }
        while(!que.isEmpty()){
            Work now = que.poll();
            boolean check = false;
            
            for(Work cnt : que){
                if(cnt.prior>now.prior){
                    check = true;
                }
            }
            if(check){
                    que.add(now);
                } else{
                    answer++;
                    if(now.location == location){
                        break;
                    }
                }
            
        }
        
        return answer;
    }
}
