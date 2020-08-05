package sec03.exam02;

public class CastingExample {

	public static void main(String[] args) {
		
		byte byteValue = 10;
		int intValue = byteValue;
		System.out.println("intValue :" + intValue);
		
		char charValue = 'K';
		intValue = charValue;
		System.out.println("Unicode for K : " + intValue);
		
		intValue = 50;
		long longValue = intValue;
		System.out.println("longValue : " + intValue);
		
		longValue = 100;
		float floatValue = longValue;
		System.out.println("floatValue : " + floatValue);
		
		floatValue = 100.5F;
		double doubleValue = floatValue;
		System.out.println("doubleValue : " + doubleValue);
		
		int valores = 44032;// Unicode de una letra
		char charval = (char)valores;
		System.out.println(charval);
		
		long longval = 500;
		valores = (int)longval;
		System.out.println(valores);
		
		double doubleval = 3.14;
		valores = (int)doubleval;
		System.out.println(valores);
		
	}

}
