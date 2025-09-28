// Use recursion to calculate the nth number in the
// Fibonacci sequence
// This is not efficient for large values of n
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc

// Import Scanner to accept user input
import java.util.Scanner;

public class Fibonacci {
    public static int fibonacci(int n) {
        // base cases
        if (n == 0 || n == 1){
            // The first and second values of the
            // Fibonacci sequence are 0 and 1
            return n;
        }
        // recursive call
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        // Define a new scanner to accept user input
        Scanner input = new Scanner(System.in);
        // Prompt the user to enter an integer index
        System.out.print("Which index value of the Fibonacci Sequence would you like to know? (Indices start at 0) ");
        // Store the users input
        int index = input.nextInt();

        // Display result
        System.out.printf("\nThe value in the Fibonacci Sequence at index %d is: %d\n", index, fibonacci(index));
    }
}