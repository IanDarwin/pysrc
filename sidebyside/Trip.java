import java.time.*;

class Trip {
	static int[] classyCabins = { 101, 102, 106, 109 }; // class field
	LocalDate start, end;	// object fields

	Trip(LocalDate start, LocalDate end) {
		this.start = start;
		this.end = end;
	}
	void printSchedule() {
		System.out.printf("Starts %s, ends %d\n", start, end);
	}
}
class Cruise extends Trip {
	String ship;
	int cabin;

	Cruise(LocalDate start, LocalDate end, String ship, int cabin) {
		super(start, end);
		this.ship = ship;
		this.cabin = cabin;
	}
	void printSchedule() {
		System.out.print("Aboard " + ship + " ");
		super.printSchedule();
	}
}
