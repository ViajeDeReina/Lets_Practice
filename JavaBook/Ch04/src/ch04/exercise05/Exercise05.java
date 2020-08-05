package ch04.exercise05;

public class Exercise05 {

	public static void main(String[] args) {
		// scattered stars *
		
		int i, j;
		
		for (i=1; i<=14; i++)
		{
			for (j=1; j <4; j++)
			{
				if (i == (j*j + 3*j)/2)
				{
					System.out.println("");
				}
			}
			System.out.print("*");
		}
	}
}
// the code is totally different from the book. Let's think more about it