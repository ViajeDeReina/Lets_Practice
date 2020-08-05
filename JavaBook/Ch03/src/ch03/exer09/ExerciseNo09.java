package ch03.exer09;

import java.util.Scanner;

public class ExerciseNo09 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("First number : ");
		double num1 = (double)Double.parseDouble(scanner.next());
		System.out.print("Second number : ");
		double num2 = (double)Double.parseDouble(scanner.next());
		System.out.println("-------------------------");
		System.out.print("Result : ");
		
		if(((int)num2 == 0) || (num2 == 0.0))
		{
			System.out.println("Infinite");
		}
		else
		{
			double resultado = num1/num2;
			System.out.println(resultado);
		}
		
	}

}
