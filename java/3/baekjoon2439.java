import java.util.Scanner;

/**
 * Created by OWNER on 2018-01-16.
 */
public class baekjoon2439
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();

        for(int i = 1; i <= N; i++)
        {
            for(int j = N - 1; j >= i; j--)
            {
                System.out.print(" ");
            }
            for(int k = 1; k <= i; k++)
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
