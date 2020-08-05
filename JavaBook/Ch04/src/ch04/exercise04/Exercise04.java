package ch04.exercise04;

public class Exercise04 {

	public static void main(String[] args) {
		// Save the sun! 4x+5y = 60;
		
		int x, y;
		
		for (x=1; x<=10; x++)
		{
			for (y=1; y<=10; y++)
			{
				if ((x*4)+(y*5) != 60)
				{continue;}
				
				System.out.printf("(%d, %d)\n",x, y);
			}
			
		}

	}

}
