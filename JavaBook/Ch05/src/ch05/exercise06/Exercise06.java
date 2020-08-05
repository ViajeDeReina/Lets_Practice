package ch05.exercise06;

import java.util.Scanner;

public class Exercise06 {

	public static void main(String[] args) {
		boolean run = true;
		int studentNum = 0;
		int [] scores = null;
		Scanner scanner = new Scanner(System.in);
		int max = 0;
		
		
		while (run)
		{
			System.out.println("------------------------------------------------------------------------");
			System.out.println("1. Student no. | 2. Input Score | 3. Load Score | 4. Analyse | 5. Exit");
			System.out.println("------------------------------------------------------------------------");
			System.out.print("Select the number > ");
			
			int selectNo = Integer.parseInt(scanner.nextLine());
			
			if (selectNo == 1)
			{
				System.out.print("Please enter the number of students : ");
				studentNum = Integer.parseInt(scanner.nextLine());
				scores = new int[studentNum];
			}
			else if (selectNo == 2)
			{
				for (int i = 0; i < scores.length; i++)
				{
					System.out.print("Please input the scores of each student : ");
					scores[i] = Integer.parseInt(scanner.nextLine());
					max = scores[0];
				}
			}
			else if (selectNo == 3)
			{
				for (int i = 0; i < scores.length; i++)
				{
					System.out.println("scores[" + i + "] > " + scores[i]);
				}
			}
			else if (selectNo == 4)
			{
				for (int i = 0; i < scores.length-1; i++)
				{
					if (max < scores[i+1])
					{
						max = scores[i+1];
					}
				}
				
				int sum = 0;
				
				for (int i = 0; i < scores.length; i++)
				{
					sum += scores[i];
				}
				
				System.out.println("Maximum Score : " + max);
				System.out.printf("Average Score : %.2f\n", (double)sum/scores.length);
			}
			else if (selectNo == 5)
			{
				run = false;
			}
		}
		
		System.out.println("The program is ended.");

	}

}
