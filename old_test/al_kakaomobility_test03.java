import java.util.*;

class Solution {
    public int solution(int[] A) {
        if(A.length<3){
            return A.length;
        }
        int cnt = 2;
        int answer =0;
        for(int i =0; i<A.length-2;i++){
            if(A[i] == A[i+2]){
                cnt++;
            } else {
               answer =  Math.max(answer,cnt);
               cnt = 2;
            }
        }
        answer =  Math.max(answer,cnt);
        return answer;
    }
}