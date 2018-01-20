import java.util.Scanner;

/**
 * Created by OWNER on 2018-01-16.
 */
public class baekjoon2440
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();

        for(int i = N; i >= 1; i--)
        {
            for(int j = i; j >= 1; j--)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}
