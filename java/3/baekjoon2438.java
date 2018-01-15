import java.util.Scanner;

/**
 * Created by OWNER on 2018-01-15.
 */
public class baekjoon2438
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();

        for(int i = 1; i <= N; i++)
        {
            for(int j = 1; j <= i; j++)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}
