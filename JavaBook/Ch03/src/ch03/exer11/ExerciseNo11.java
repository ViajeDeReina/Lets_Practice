package ch03.exer11;

import java.util.Scanner;

public class ExerciseNo11 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("Please enter ID : ");
		String name = scanner.nextLine();
		
		System.out.print("Please enter password : ");
		int passwd = (int)Integer.parseInt(scanner.nextLine());
		
		if (name == "java")
		{
			if (passwd == 12345)
			{
				System.out.println("You've successfully signed in.");
			}
			else
			{
				System.out.println("You've got wrong password.");
				
			}
		}
		else
		{
			System.out.println("The ID doesn't exist.");
		}

	}

}
