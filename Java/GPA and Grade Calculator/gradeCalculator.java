import java.util.Scanner;

public class gradeCalculator {
	Scanner funct;
	Scanner scan;
	
	public static void main(String[] args) {
		gradeCalculator call = new gradeCalculator();
		call.funct = new Scanner(System.in);
		call.scan = new Scanner(System.in);
		call.options();
		
	}
	
	public void options() {
		System.out.println("Would you like to calculate a course grade or GPA in percent and 4.0 scale. Enter c for course, g for gpa, or e to exit.");
		char option;
		
		try {
			option = funct.nextLine().charAt(0);
			
		}
		
		catch (Exception e) {
			funct.close();
			scan.close();
			return;
			
		}
		
		if (option == 'c') {
			gradecalc();
			
		}
		
		else if (option == 'g') {
			gpacalc();
			
		}
		
		else if (option == 'e') {
			funct.close();
			scan.close();
			return;
			
		}
		
		else {
			System.out.println("Invalid input entered.");
			System.out.println("\n");
			options();
			
		}
	}
	
	public float gpaconvert(float percent) {
		float gpa;
		
		if (percent < 50) {
			gpa = 0;
			
		}
		
		else if (percent < 53) {
			gpa = (float) 0.7;
			
		}
		
		else if (percent < 57) {
			gpa = 1;
			
		}
		
		else if (percent < 60) {
			gpa = (float) 1.3;
			
		}
		
		else if (percent < 63) {
			gpa = (float) 1.7;
			
		}
		
		else if (percent < 67) {
			gpa = 2;
			
		}
		
		else if (percent < 70) {
			gpa = (float) 2.3;
			
		}
		
		else if (percent < 73) {
			gpa = (float) 2.7;
			
		}
		
		else if (percent < 77) {
			gpa = 3;
			
		}
		
		else if (percent < 80) {
			gpa = (float) 3.3;
			
		}
		
		else if (percent < 85) {
			gpa = (float) 3.7;
			
		}
		
		else if (percent < 90) {
			gpa = (float) 3.9;
			
		}
		
		else {
			gpa = 4;
			
		}
		
		return gpa;
		
	}
	
	public void gpacalc() {
		boolean more = true;
		float current = 0;
		float creditamount = 0;
		
		while (more == true) {
			scan = new Scanner(System.in);
			
			try {
				System.out.print("Grade: ");
				String gradestr = scan.nextLine();
				float grade = Float.parseFloat(gradestr);
				
				System.out.print("Credits (0.5 per semester): ");
				float credits = scan.nextFloat();
				credits = credits * 2;
				
				current += (grade * credits);
				creditamount += credits;
				
			}
		
			catch (Exception e) {
				more = false;
				
			}
		}
			
		float gpaPercent = current/creditamount;
			
		System.out.print("Current GPA in % is: ");
		System.out.println(gpaPercent);
			
		float gpa = gpaconvert(gpaPercent);
		System.out.print("\nCurrent GPA on 4.0 scale is: ");
		System.out.println(gpa);
		System.out.println("\n");
		
		options();
		
	}
	
	
	public void gradecalc() {
		boolean more = true;
		float current = 0;
		float percentamount = 0;
		float target = 0;
		
		while (more == true && percentamount < 1) {
			scan = new Scanner(System.in);
			
			try {
				System.out.print("Grade: ");
				String gradestr = scan.nextLine();
				float grade = Float.parseFloat(gradestr);
				
				System.out.print("Assignment Weight: ");
				float percent = scan.nextFloat();
				
				current += (grade*(percent/100));
				percentamount += percent/100;
				
			}
		
			catch (Exception e) {
				more = false;
				System.out.print("Target Grade: ");
				target = scan.nextFloat();
				
			}
		}
		
		System.out.print("Current Percent Total: ");
		System.out.println(current);
		
		
		if (percentamount != 1 && current < target) {
			float need = (target - current) / (1 - percentamount);
			System.out.print("Avg needed on remaining weight to get ");
			System.out.print(target);
			System.out.print("%: ");
			System.out.println(need);
			
		}
		
		else if (current >= target && percentamount != 1) {
			System.out.print("Current grade is already greater then or equal to ");
			System.out.println(target);
		}
		
		System.out.println("\n");
		options();
		
	}
}
