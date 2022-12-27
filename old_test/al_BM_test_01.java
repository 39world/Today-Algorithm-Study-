import java.util.*;
import java.util.stream.Collectors;
// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public String solution(int U, int L, int[] C) {
        
        int sum = 0;
        int countTwo = 0;
        int countOne = 0;
        for (int i = 0 ; i< C.length ; i++){
            sum += C[i];
        }
        if (sum != U+L){ //불가능한 경우
            String result = "IMPOSSIBLE";

            return result;
        }
        int[][] array = new int[2][C.length];

        for (int j = 0 ; j<C.length ; j++){ //공통으로 들어가는 1 넣어주기
            if (C[j]==2){
                array[0][j] = 1;
                array[1][j] = 1;
                countTwo += 1;
            }
        }

        for (int k = 0 ; k<C.length ; k++){ //첫번째 행부터 차례대로 1 넣어주기
            if (C[k] == 0){
                array[0][k] = 0;
                array[1][k] = 0;
          }
            else if (C[k] == 1 && countTwo+countOne < U) {
                array[0][k] = 1;
                array[1][k] = 0;
                countOne += 1;
            }
            else if (C[k] == 1 && countTwo+countOne == U){
                array[0][k] = 0;
                array[1][k] = 1;
            }
        }
        String result ="";
        for (int i = 0 ; i<2;i++){ //숫자 배열을 문자열로 바궈주기
            if (i == 1){ //행 과 행 사이 , 추가하기
                result +=",";
            }
            for (int j = 0 ; j<C.length;j++){
                result += String.valueOf(array[i][j]); 
            }
            
        }        
        return result;
    }
}
