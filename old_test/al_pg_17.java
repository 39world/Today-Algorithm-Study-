#프로그래머스 카카오프렌즈 컬러링북


class Solution {
    
    static int numberOfArea;
    static int maxSizeOfOneArea;
    static int checkCnt;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    
    public static void colorCheck(int x, int y, boolean[][] check, int[][] picture){
        if(check[x][y]) return;
        
        check[x][y] = true;
        
        checkCnt++;
        for(int i =0;i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx<0 || nx>=picture.length || ny<0 || ny>=picture[0].length) continue;
            
            if(picture[nx][ny] == picture[x][y] && !check[nx][ny]){
                colorCheck(nx,ny,check,picture);
            }
            
        }
        
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        numberOfArea = 0;
        maxSizeOfOneArea = 0;

        boolean[][] check = new boolean[m][n];
        checkCnt = 0;
        
        for(int i = 0; i<m; i++){
            for(int j = 0 ; j<n ; j++){
                if(!check[i][j] && picture[i][j] != 0){    
                    numberOfArea++;
                    colorCheck(i,j,check,picture);
                }
                
                if(checkCnt > maxSizeOfOneArea){
                    maxSizeOfOneArea = checkCnt;
                }
                checkCnt = 0;
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    
}