// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public String solution(String S) {
        int music = 0 ;
        int images = 0;
        int movies = 0;
        int other = 0;
        String musicArray[] = {"mp3","aac","flac"};
        String imageArray[] = {"jpg","bmp","gif"};
        String movieArray[] = {"mp4","avi","mkv"};

        String[] drive = S.split("\n"); //한 줄씩 나누기
        for (int i = 0 ; i< drive.length ; i++){
            String[] array = drive[i].split(" ");  //파일과 용량 나누기
            String[] file = array[0].split("[.]"); // 파일명 나누기
            if(Arrays.asList(musicArray).contains(file[file.length-1])){ //파일명 비교하여 용량 더하기
                String space = array[1].replaceAll("[^0-9]", "");
                music +=  Integer.parseInt(space);                
            }
            else if(Arrays.asList(imageArray).contains(file[file.length-1])){
                String space = array[1].replaceAll("[^0-9]", "");
                images +=  Integer.parseInt(space);  
            }
            else if(Arrays.asList(movieArray).contains(file[file.length-1])){
                String space = array[1].replaceAll("[^0-9]", "");
                movies +=  Integer.parseInt(space);  
            }
            else{
                String space = array[1].replaceAll("[^0-9]", "");
                other +=  Integer.parseInt(space);  
            }
        } //출력값 만들어주기 
        String result = "music "+String.valueOf(music)+"b\n"+"images "+String.valueOf(images)+"b\n"+"movies "+String.valueOf(movies)+"b\n"+"other "+String.valueOf(other)+"b";
        return result;
    }
}
