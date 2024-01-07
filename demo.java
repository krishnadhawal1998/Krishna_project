package demo;
public class CheckPalindrome {
    public static void palindrome(int number) {
        int rev = 0, store, n1, left;
        n1 = number;
        store = number;  
        while(number > 0) {
            left = number / 10; 10
            rev = rev + 10 * left; 100
            number = number % 10; =1
        }
        if(n1 == rev) {
            System.out.print("Number " + n1 + " is Palindrome number");
        } else {
            System.out.print("it is not a Palindrome number");
        }
    }
}