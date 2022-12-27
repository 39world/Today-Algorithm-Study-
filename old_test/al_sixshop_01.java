class Solution {
    public int solution(int[] estimates, int k) {
        int answer = 0;
        
        for(int i = 1 ; i<estimates.length;i++){
            estimates[i] = estimates[i] +  estimates[i-1];
        }
        
        answer = estimates[k-1];
        
        int totalUser = 0;
        
        for(int i = k ; i<estimates.length ; i++){
            totalUser = estimates[i] - estimates[i-k];
            if(totalUser > answer ) answer = totalUser;
        }
        
        return answer;
    }
}