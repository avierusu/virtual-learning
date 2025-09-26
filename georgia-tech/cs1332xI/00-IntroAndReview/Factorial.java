// Use recursion to calculate the factorial of n
// n! is calculated using the following formula:
// n * n-1 * n-2 * n-3 * ... * 2 * 1

// Import Scanner to accept user input
import java.util.Scanner;

public class Factorial {
    public static int factorial(int n) {
        if (n <= 1) {
            // base case
            return 1;
        }
        // recursive call
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        // Define a new scanner to accept user input
        Scanner input = new Scanner(System.in);
        // Prompt the user to enter an integer
        System.out.print("Enter an integer to calculate the factorial of: ");
        // Store the users input
        int value = input.nextInt();

        // Dipslay the result
        System.out.printf("Factorial of %d: %d\n", value, factorial(value));
    }
}