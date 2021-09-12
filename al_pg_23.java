#프로그래머스 등굣길 
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        
        int[][] map = new int[n+1][m+1];
        for(int[] water : puddles){
            map[water[1]][water[0]] = -1;            
        }
        map[1][1] = 1;
        
        for(int i = 1; i<=n;i++){
            for(int j = 1; j<=m;j++){
                if(map[i][j] == -1){
                    map[i][j] = 0;
                    continue;
                }                    
                if(i !=1) 
                    map[i][j] += map[i-1][j] % 1000000007;
                if(j !=1) 
                    map[i][j] += map[i][j-1] % 1000000007;                
                }            
        }
        answer = map[n][m]%1000000007;
        return answer;
    }    
}