import java.util.Scanner;
 
public class Main{
     public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         int N = sc.nextInt();
 
        int [][] arr = new int[N][N];
         int x = -1 , y = -1;
         int num = 0;
         for(int i = 0 ; i < N; ++i)
         {
             for(int j = i; j < N; ++j)
             {
                 if(i%3 == 0)
                 {
                     x++; y++;
                 }else if(i%3 == 1)
                 {
                     y--;
                 }else if(i%3 == 2)
                 {
                     x--;
                 }
                 arr[x][y] = (num++)%10;
             }
         }
 
 
         for(int i = 0; i < N; ++i)
         {
             for(int j = 0; j < i+1; ++j)
             {
                 System.out.print(arr[i][j]+ " ");
             }System.out.println();
         }
 
    }
 }


출처: https://dyndy.tistory.com/82 [DY N DY]