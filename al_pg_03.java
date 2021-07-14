class Solution {
    public int solution(int n) {
        int answer = n;
        String b = Integer.toBinaryString(n);
        int num = 0;
        for(char c : b.toCharArray()){
            if(c=='1')num++;
        }
        
        for(answer=n+1;answer<1000000;answer++){
            b = Integer.toBinaryString(answer);
            int a = 0;
             for(char c : b.toCharArray()){
                if(c=='1')a++;
             }
            if(num==a)return answer;
            
        }
        return answer;
    }
}