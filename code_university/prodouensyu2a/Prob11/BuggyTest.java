package prob11b;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BuggyTest {

	@Test
	void test1() {
		try {
			Buggy aBuggy = new Buggy();
			assertEquals(true,aBuggy.isPerfect(6));
		}
		catch(Exception e) {
			System.out.println("Error");
		}
	}
	@Test
	void test2() {
		try {
			Buggy aBuggy = new Buggy();
			assertEquals(true,aBuggy.isPerfect(28));
		}
		catch(Exception e) {
			System.out.println("Error");
		}
	}
	@Test
	void test3() {
		try {
			Buggy aBuggy = new Buggy();
			assertEquals(true,aBuggy.isPerfect(496));
		}
		catch(Exception e) {
			System.out.println("Error");
		}
	}
	@Test
	void test4() {
		try {
			Buggy aBuggy = new Buggy();
			for (int i=1;i<=1000;i++) {
				if (i==6||i==28||i==496) {
					assertEquals(false,aBuggy.isPerfect(i));
				}
			}
		}
		catch(Exception e) {
			System.out.println("Error");
		}
	}
}
