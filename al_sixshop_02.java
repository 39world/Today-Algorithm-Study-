import java.util.*;

class Solution {
    public int solution(int K, String[] user_scores) {        
        
        int answer = 0;
                
        List<String> ranking = new ArrayList<>();
        List<Integer> scoreList = new ArrayList<>();
        String userId = new String();
        int score = 0;
        for(String record : user_scores){
            String[] split = record.split(" ");
            userId = split[0];
            score = Integer.parseInt(split[1]);
            int index = ranking.indexOf(userId);
            if(index != -1){ //이전에 등록한 값이 존재
                int rankingIndex = ranking.indexOf(userId);
                if(scoreList.get(rankingIndex)<score){ //점수가 올랐을 때
                    
                    for(int i = 0 ; i<scoreList.size();i++){
                      if(scoreList.get(i) < score){ //등수 찾기
                        if(i != rankingIndex && i<K) answer++; //등수가 변했을 때          
                        ranking.remove(rankingIndex);
                        scoreList.remove(rankingIndex);
                        ranking.add(i,userId);
                        scoreList.add(i,score);
                        break;
                      }
                    } 
                }
            }else { 
                for(int i = 0 ; i<=scoreList.size();i++){
                    if(i == scoreList.size()){ //끝 혹은 처음 값
                        ranking.add(userId);
                        scoreList.add(score);
                        if(i<K) answer++;
                        break;
                    }
                    if(scoreList.get(i) < score){ //중간
                        ranking.add(i,userId);
                        scoreList.add(i,score);
                        if(i<K) answer++;                        
                        break;
                    }
                }
                
            }  
        }
        
        return answer;
    }
}