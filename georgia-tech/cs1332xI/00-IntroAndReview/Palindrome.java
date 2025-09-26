// Use recursion to determine if a string is a palindrome

// Import Scanner to accept user input
import java.util.Scanner;

public class Palindrome {
    public static boolean isPalindrome(String str, int start, int end){
        // base cases
        if (start >= end){
            // If we have checked every letter and we have passed
            // halfway into the word, then it is a palindrome
            return true;
        }
        if (str.charAt(start) != str.charAt(end)){
            return false;
        }

        // recursive step
        return isPalindrome(str, start + 1, end - 1);
    }

    public static void main(String[] args) {
        // Define a new scanner to accept user input
        Scanner input = new Scanner(System.in);
        // Prompt the user to enter an integer index
        System.out.print("Enter a word to determine if it is a palindrome: ");
        // Store the users input
        String word = input.nextLine();

        // Display result
        System.out.println("Is palindrome? " + isPalindrome(word, 0, word.length() - 1));
    }
}