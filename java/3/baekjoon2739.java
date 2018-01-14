import java.util.Scanner;

/**
 * Created by OWNER on 2018-01-14.
 */
public class baekjoon2739
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();

        for(int i = 1; i <= 9; i++)
        {
            System.out.println(N + " * "+ i + " = " + N * i);
        }
    }
}
