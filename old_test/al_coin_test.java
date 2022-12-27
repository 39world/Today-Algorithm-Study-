## 엑셀 파일을 읽어 캔들 만들기 과제 

import java.text.DecimalFormat;
import java.util.*;

import jdk.nashorn.internal.runtime.JSONListAdapter;

public class coin {
    //CSV Parsing은 이미 만들어져있는 상태로 가정하여 파싱을 통해 String 데이터가 들어온 다음 과정을 정리.
    static String[] sample = {"1383038122,250000,2.00000000","1383038169,254000,0.09700000","1383038169,259000,1.90300000","1383038233,251000,1.39100000"}; //샘플 데이터 일부
    static DecimalFormat form = new DecimalFormat("#.00000000"); //거래량의 사토시 단위를 맞추기 위함.
    public static class ResultCandle{

        Integer start;  //시작 시간
        Integer end;    //끝나는 시간
        String open;    //시가
        String close;   //종가
        String high;    //고가
        String low;     //저가
        String average; //거래된 평균가격
        String weighted_average;    //가중산술평균 (가격x해당 가격 거래량 / 정해진 시간 토탈 거래량) 의 합
        String volume; //거래량

        public ResultCandle(int start, int end, String open, String close, String high, String low, String average, String weighted, String volume){
            this.start = start;
            this.end = end;
            this.open = open;
            this.close = close;
            this.high = high;
            this.low = low;
            this.average = average;
            this.weighted_average = weighted;
            this.volume = volume;            
        }
    }

    public static class TempCandle{ //임시 캔들 데이터 계산을 쉽게 하기 위해 Integer 과 Double로 이루어진 캔들로 데이터를 모아간다.
        Integer start;  
        Integer end;    
        Integer open;    
        Integer close;   
        Integer high;    
        Integer low;     
        Double average; 
        Double weighted_average;    
        Double volume; 
    }

    public static List<ResultCandle> makeCandle(Integer size, String[] sample){
        
        List<ResultCandle> result = new ArrayList<>(); //만들어진 캔들 리스트

        //항상 첫 번째 값의 시간이 기준이므로 첫 번째 샘플 데이터로 시작하는 기준 시간을 잡고 임시 캔들 데이터를 셋팅
        String firstSample = sample[0];
        String[] splitRecord = firstSample.split(",");
        Integer time = Integer.parseInt(splitRecord[0]);

        TempCandle tempCandle = new TempCandle();
        tempCandle.start = time;
        tempCandle.end = time+size-1;
        tempCandle.open = Integer.parseInt(splitRecord[1]);
        tempCandle.close = Integer.parseInt(splitRecord[1]);
        tempCandle.high = Integer.parseInt(splitRecord[1]);
        tempCandle.low = Integer.parseInt(splitRecord[1]);
        tempCandle.average = Double.parseDouble(splitRecord[1]);
        tempCandle.weighted_average = Double.parseDouble(splitRecord[1])*Double.parseDouble(splitRecord[2]);  
        tempCandle.volume = Double.parseDouble(splitRecord[2]);        

        double cnt = 1.0; //평균 값을 내기 위해 각 캔들당 몇개의 샘플 데이터가 들어갔는지 측정한다.

        for(int i =1 ; i<sample.length; i++){
            splitRecord = sample[i].split(",");            
            if( Integer.parseInt(splitRecord[0]) > tempCandle.end){ //다음 샘플 데이터의 시간이 주어진 시간 간격을 넘었다면
                                  
               //임시 캔들 값을 이용해 캔들 생성, 결과 리스트에 추가
                result.add(new ResultCandle(tempCandle.start,tempCandle.end,Integer.toString(tempCandle.open),Integer.toString(tempCandle.close),Integer.toString(tempCandle.high),
                Integer.toString(tempCandle.low),Integer.toString((int) Math.round(tempCandle.average/cnt)),Integer.toString((int) Math.round(tempCandle.weighted_average/tempCandle.volume)),
                Double.toString(tempCandle.volume)));
                
                
                //새로운 임시 캔들 생성
                time = time + size; 
                tempCandle = new TempCandle();                 
                tempCandle.start = time;
                tempCandle.end = time+size-1;
                if( Integer.parseInt(splitRecord[0]) > tempCandle.end){ //현재 샘플 데이터가 바로 다음 시간대에 속하지 않는다면 null값으로 이루어진 캔들 생성 후 해당 시간대가 나올 때까지 반복
                    while(tempCandle.end < Integer.parseInt(splitRecord[0])){
                        result.add(new ResultCandle(tempCandle.start, tempCandle.end, null, null, null, null, null, null, "0.00000000"));
                        time = time + size; 
                        tempCandle = new TempCandle();                 
                        tempCandle.start = time;
                        tempCandle.end = time+size-1;
                    }                   
                } 
                tempCandle.open = Integer.parseInt(splitRecord[1]);
                tempCandle.close = Integer.parseInt(splitRecord[1]);
                tempCandle.high = Integer.parseInt(splitRecord[1]);
                tempCandle.low = Integer.parseInt(splitRecord[1]);
                tempCandle.average = Double.parseDouble(splitRecord[1]);
                tempCandle.weighted_average = Double.parseDouble(splitRecord[1])*Double.parseDouble(splitRecord[2]);  
                tempCandle.volume = Double.parseDouble(splitRecord[2]); 
                cnt = 1.0;  

                if(i == sample.length-1){ //마지막 샘플 데이터였다면 캔들로 만들어서 결과 리스트에 출력해주기
                    result.add(new ResultCandle(tempCandle.start,tempCandle.end,Integer.toString(tempCandle.open),Integer.toString(tempCandle.close),Integer.toString(tempCandle.high),
                Integer.toString(tempCandle.low),Integer.toString((int) Math.round(tempCandle.average/cnt)),Integer.toString((int) Math.round(tempCandle.weighted_average/tempCandle.volume)),
                form.format(tempCandle.volume)));
                }
                
                

            } else { //다음 샘플 데이터의 시간이 주어진 시간 간격 사이라면
                cnt += 1.0;        

                tempCandle.close = Integer.parseInt(splitRecord[1]); //종가 수정해주기

                Integer price = Integer.parseInt(splitRecord[1]);

                if(price > tempCandle.high){ //신고가인지 확인
                    tempCandle.high = Integer.parseInt(splitRecord[1]);
                } else if(price <tempCandle.low){// 신저가인지 확인
                    tempCandle.high = Integer.parseInt(splitRecord[1]);
                } 
                //데이터의 가격과 가중치가 곱해진 가격을 각각 기존 값에 더해가며 모은 후 캔들 생성시 나눠준다.
                tempCandle.average += Double.parseDouble(splitRecord[1]);
                tempCandle.weighted_average +=  Double.parseDouble(splitRecord[1])*Double.parseDouble(splitRecord[2]);
                tempCandle.volume += Double.parseDouble(splitRecord[2]);   
            }

        }

        return result;
    }



    public static void main(String[] args){

        List<ResultCandle> result = coin.makeCandle(30,sample); //요구되는 Output에 해당하는 리스트 값. 프론트로 반환해주면 JSON 형식으로 반환 완료.     
        
        
        for(ResultCandle eachCandle : result){ //각 데이터 확인을 위함
            System.out.println(eachCandle.start);
            System.out.println(eachCandle.end);
            System.out.println(eachCandle.open);
            System.out.println(eachCandle.close);
            System.out.println(eachCandle.high);
            System.out.println(eachCandle.low);
            System.out.println(eachCandle.average);
            System.out.println(eachCandle.weighted_average);
            System.out.println(eachCandle.volume);
            System.out.println("");
        }
    }
}