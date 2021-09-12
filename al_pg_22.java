#프로그래머스 네트워크
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] check = new boolean[n];
        for(int i = 0 ; i<n ; i++){
            if(!check[i]){
                dfs(computers,i,check);
                answer++;
            }
        }
        
        return answer;
    }
    
    public void dfs(int[][] computers, int i, boolean[] check){
        check[i] = true;
        
        for(int j =0; j<computers[i].length; j++){
            if(i != j && check[j] == false && computers[i][j] == 1){
                dfs(computers,j,check);
            }
        }
    }
}