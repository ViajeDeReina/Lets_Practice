package ch04.exam04;

public class IfDiceExample {

	public static void main(String[] args) throws Exception {
		
		System.out.print("Press 'a' to throw the dice. ('q' for exit) : ");
		char inputval = (char)System.in.read();
		
		while (inputval != 'q')
		{
			if(inputval == 'a')
			{
				int randnum = (int)(Math.random()*6) + 1;
				
				if (randnum == 1) {System.out.println("You've got 1.");}
				if (randnum == 2) {System.out.println("You've got 2.");}
				if (randnum == 3) {System.out.println("You've got 3.");}
				if (randnum == 4) {System.out.println("You've got 4.");}
				if (randnum == 5) {System.out.println("You've got 5.");}
				if (randnum == 6) {System.out.println("You've got 6.");}
			}
			else {System.out.println("Command not available.");}
			
			System.out.print("Press 'a' to throw the dice. ('q' for exit) : ");
			inputval = (char)System.in.read();
		}
	}
}
