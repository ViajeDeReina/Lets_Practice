package ch04.exam02;
import java.util.Scanner;

public class IfElseExample {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("Please enter your score. : ");
		int score = (int)Integer.parseInt(scanner.next());
		
		if (score >= 90)
		{
			System.out.println("You've done a good job.\nGrade : A");
		}
		else
		{
			System.out.println("......:b");
		}
	}

}
