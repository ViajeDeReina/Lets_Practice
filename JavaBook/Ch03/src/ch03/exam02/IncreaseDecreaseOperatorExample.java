package ch03.exam02;

public class IncreaseDecreaseOperatorExample {

	public static void main(String[] args) {
		
		int x = 10;
		int y = 10;
		int z;
		
		System.out.println("----------------------------------");
		x++;
		++x;
		System.out.println("x = " + x);
		
		System.out.println("----------------------------------");
		y--;
		--y;
		System.out.println("y = " + y);
		
		System.out.println("----------------------------------");
		z = x++;
		System.out.println("z = " + z);// when x=12, z=x=12, after then x increased
		System.out.println("x = " + x);//thus x=13 here
		
		System.out.println("----------------------------------");
		z = ++x;
		System.out.println("z = " + z);
		System.out.println("x = " + x);
		
		System.out.println("----------------------------------");
		z = ++x + y++;
		System.out.println("z = " + z);
		System.out.println("x = " + x);
		System.out.println("y = " + y);

	}

}
