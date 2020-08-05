package ch04.exercise07;

import java.util.Scanner;

public class Exercise07 {

	public static void main(String[] args) {
		// This is quite challenging.... :9
		
		boolean run = true;
		int balance = 0;
		Scanner scanner = new Scanner (System.in);
		
		while (run)
		{
			System.out.println("---------------------------------------");
			System.out.println("1. Deposit / 2. Withdraw / 3. Current Saving / 4. Exit");
			System.out.println("---------------------------------------");
			System.out.print("Please select > ");
			int selec = (int)Integer.parseInt(scanner.nextLine());
			
			switch(selec)
			{
			case 1:
			{System.out.print("Deposit amount : ");
			int deposit = (int)Integer.parseInt(scanner.nextLine());
			balance += deposit;
			break;
			}
			case 2:
			{System.out.print("Withdraw amount : ");
			int withdraw = (int)Integer.parseInt(scanner.nextLine());
			balance -= withdraw;
			break;
			}
			case 3:
			{
				System.out.println("Current Saving : " + balance);
				break;
			}
			default :{run = false;}
			
		}

	}
		System.out.println("Thank you for using our bank. Bye.");

}
}
