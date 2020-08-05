package ch04.exam01;
import java.util.Scanner;

public class IfExample {

	public static void main(String[] args) {
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("Please enter your score : ");
		int score = (int)Integer.parseInt(scanner.next());
		
		if (score >= 90)
		{
			System.out.println("You've done a good job.\nGrade : A");
		}
		if (score < 90)
		{
			System.out.println("......:b");
		}

	}

}
