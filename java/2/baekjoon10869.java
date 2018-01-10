import java.util.Scanner;

/**
 * Created by OWNER on 2018-01-10.
 */
public class baekjoon10869
{
    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        int A, B;

        A = input.nextInt();
        B = input.nextInt();

        System.out.println(A + B);
        System.out.println(A - B);
        System.out.println(A * B);
        System.out.println(A / B);
        System.out.println(A % B);
    }
}
