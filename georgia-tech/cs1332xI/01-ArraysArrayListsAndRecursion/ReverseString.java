// Use recursion to reverse the order of a string

// Import Scanner to accept user input
import java.util.Scanner;

public class ReverseString {
    public static String reverse(String str) {
        // base case
        if (str.isEmpty()){
            return str;
        }
        // recursive call
        return reverse(str.substring(1)) + str.charAt(0);
    }

    public static void main(String[] args) {
        // Define a new scanner to accept user input
        Scanner input = new Scanner(System.in);
        // Prompt the user to enter an integer index
        System.out.print("Enter a phrase to reverse: ");
        // Store the users input
        String phrase = input.nextLine();

        // Display the reversed string
        System.out.println("Reversed: " + reverse(phrase));
    }
}