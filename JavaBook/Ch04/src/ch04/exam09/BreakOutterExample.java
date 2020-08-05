package ch04.exam09;

public class BreakOutterExample {

	public static void main(String[] args) {
		
		//available only within label Outter block
		Outter: for (char upper = 'A'; upper<= 'Z'; upper++) {
			for (char lower = 'a'; lower <='z'; lower++) {
				System.out.println(upper + "-" + lower);
				if (lower == 'g') {
					break Outter;// when lower == g, ALL STOP, without hesitation, just stop
				}
			}
		}
	
	System.out.println("The program is shut down");

	}
}
// further comments : 1st loop (upper character) will be repeated increasing its size till Z.
//2nd loop (lower character) will also be repeated increasing by 1
// HOWEVER, when lower == g, the program will be shut down, by its condition. break Outter;