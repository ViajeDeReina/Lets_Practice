package ch05.exercise04;

public class Exercise04 {

	public static void main(String[] args) {
		int max = 0;
		int[] array = {1, 3, 5, 8, 2};
		
		for (int i = 0; i < array.length-1; i++)
		{
			max = array[i];
			
			if (array[i] < array[i+1])
			{
				max = array[i+1];
			}
		}
		
		System.out.println("max : " + max);

	}

}
