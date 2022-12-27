// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        int tempNumber = 0;
        int result = 0;
        Arrays.sort(A);
        for (int i = 0 ; i<A.length; i++){
            tempNumber =  A[i] * (-1);
            for(int j = A.length-1 ; j>0; j--){
                if(A[j] == tempNumber){                    
                    result = Math.abs(tempNumber);
                    return result;                    
                }
            }
        }        
        return result;
    }
}
