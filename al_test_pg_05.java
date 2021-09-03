##프로그래머스 코딩테스트 순위 검색 자바 

import java.util.*;

class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        
        List<String> allcase =new ArrayList<String>();
        String tempcase = new String();
        for(int i =0; i<2; i++){
            tempcase = tempcase.substring(0,0);
            tempcase = tempcase+Integer.toString(i);
            for(int j = 0; j<2;j++){
                tempcase = tempcase.substring(0,1);
                tempcase = tempcase+Integer.toString(j);
                for(int k = 0 ; k<2; k++){
                    tempcase = tempcase.substring(0,2);
                    tempcase = tempcase+Integer.toString(k);
                    for(int z = 0; z<2 ; z++){
                        tempcase = tempcase+Integer.toString(z);                        
                        allcase.add(tempcase);
                        tempcase = tempcase.substring(0,3);
                    }
                }
            }
        }
        
        
        Map<String, List<Integer>> map = new HashMap<>();
        String key = new String();
        for (String in : info) {
            String[] split = in.split(" ");
            int score = Integer.parseInt(split[4]);
            for(int i = 0; i<16 ; i++){
                key = new String();
                String nowcase = allcase.get(i);
                for(int j =0; j<4;j++){
                    if(nowcase.charAt(j) == (char) '0'){
                        key = key+"-";
                    }
                    else {
                        key = key+split[j];                        
                    }                    
                }
                map.computeIfAbsent(key.toString(), s -> new ArrayList<>()).add(score);
            }
        }
        
        for(Map.Entry<String, List<Integer>> entry : map.entrySet()){
            entry.getValue().sort(null);
        }
        
        for (int i=0; i<query.length;i++) {
            String[] split = query[i].replaceAll(" and ","").split(" ");
           
            key = split[0];            
            int score = Integer.parseInt(split[1]);
            List<Integer> scores = map.get(key);
            int start = 0;
            int end = scores.size();
            
            while(start<end){
                int mid = (start+end)/2;
                if(scores.get(mid) < score){
                    start = mid+1;                
                }
                else {
                    end = mid;
                }                    
            }
            answer[i]=scores.size()-start;
        } 
        return answer;
    }

}