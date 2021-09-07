import java.util.*;

class Solution {
    public String solution(String S, String C) {
        List<String> nameList = new ArrayList<String>();
        String answer = new String();
        String[] names = S.split(", ");
        String email = new String();
        C = C.toLowerCase();
        for(int i = 0; i<names.length; i++){
            String name = names[i];
            String[] split = name.split(" ");
            if(split.length == 3){
                String first = split[0].substring(0,1);
                first = first.toLowerCase();
                String second = split[1].substring(0,1);
                second = second.toLowerCase();
                split[2] = split[2].replaceAll("-","");
                String last = split[2].substring(0,Math.min(8,split[2].length()));
                last = last.toLowerCase();
                int cnt =1;
                String id = first+second+last;
                while(nameList.contains(id)){                
                cnt++;
                id = first+second+last+Integer.toString(cnt);
                }
                email = id+"@"+C+".com";
                nameList.add(id);   
            } else {
                String first = split[0].substring(0,1);
                first = first.toLowerCase();
                String last = split[1].substring(0,Math.min(8,split[1].length()));
                last = last.toLowerCase();
                String id = first+last;
                int cnt = 1;
                while(nameList.contains(id)){
                cnt++;
                id = first+last+Integer.toString(cnt);
                }
                email = id+"@"+C+".com";                
                nameList.add(id);  
            }

            if(names.length == 1){
                answer += name;
                answer += " <"+email+">.";
                return answer;
            }

            if(i ==0){
                answer += name;
                answer += " <"+email+">";
            } else if(i== names.length-1){
                answer += ", "+name;
                answer += " <"+email+">";                
            } else{
                answer += ", "+name;
                answer += " <"+email+">";
            }
            
        }
        return answer;
    }
}
