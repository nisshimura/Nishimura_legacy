import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
public class Buggy {
	public boolean isPerfect(int num) {
		int sum= 0;
		for(int i=1; i < num/2; i++){
			if(num % i == 0){
				sum+= i;
			}
		}
		return (sum == num);
	}

	@Test
	void test(){

	}

}
