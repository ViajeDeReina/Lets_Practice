package ch05.exercise05;

public class Exercise05 {

	public static void main(String[] args) {
		int[][] array = {
				{95, 86},
				{83, 92, 96},
				{78, 83, 93, 87, 88}
		};
		
		int sum = 0;
		double avg = 0.0;
		
		int ttlLength = 0;
		
		for (int i = 0; i < array.length; i++)
		{
			for (int j=0; j < array[i].length; j++)
			{
				sum += array[i][j];
				ttlLength++;
			}
		}
		
		avg = (double)sum/ttlLength;
		
		System.out.println("sum : " + sum);
		System.out.println("average : " + avg);

	}

}
