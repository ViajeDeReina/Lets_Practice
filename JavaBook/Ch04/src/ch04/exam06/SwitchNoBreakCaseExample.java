package ch04.exam06;

public class SwitchNoBreakCaseExample {

	public static void main(String[] args) {
		
		int time = (int)(Math.random() *4) + 8; // will choose a random digit from the range of 4 digits, within 8~11
		System.out.println("[Current time : " + time + " O'Clock]");
		
		switch (time)
		{
		case 8:
			System.out.println("You should go to work.");
		case 9:
			System.out.println("Time to have a meeting.");
		case 10:
			System.out.println("Submit the report.");
		case 11:
			System.out.println("Have lunch.");
		}

	}

}
