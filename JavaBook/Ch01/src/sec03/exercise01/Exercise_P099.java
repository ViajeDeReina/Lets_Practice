package sec03.exercise01;

import java.util.Scanner;

public class Exercise_P099 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner (System.in);
		
		System.out.println("[Input essential information]");
		System.out.print("1. Name : ");
		String name = scanner.nextLine();
		System.out.print("2. National ID 6 digits : ");
		String NID = scanner.nextLine();
		System.out.print("3. Tel. : ");
		String tele = scanner.nextLine();
		
		System.out.println("\n[Input data]");
		System.out.printf("%s\n%s\n%s\n",name, NID, tele);

	}

}
