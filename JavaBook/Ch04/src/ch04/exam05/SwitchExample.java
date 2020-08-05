package ch04.exam05;

public class SwitchExample {
	
public static void main(String[] args) throws Exception {
		
		System.out.print("Press 'a' to throw the dice. ('q' for exit) : ");
		char inputval = (char)System.in.read();
		
		while (inputval != 'q')
		{
			if(inputval == 'a')
			{
				int randnum = (int)(Math.random()*6) + 1;
				
				switch(randnum)
				{
				case 1:
					System.out.println("You've got 1.");
					break;
				case 2:
					System.out.println("You've got 2.");
					break;
				case 3:
					System.out.println("You've got 3.");
					break;
				case 4:
					System.out.println("You've got 4.");
					break;
				case 5:
					System.out.println("You've got 5.");
					break;
				case 6:
					System.out.println("You've got 6.");
					break;
				}
			}
			
			else {System.out.println("Command not available.");}
			
			System.out.print("Press 'a' to throw the dice. ('q' for exit) : ");
			inputval = (char)System.in.read();
		}
	}
}
