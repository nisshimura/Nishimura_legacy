import java.util.ArrayList;
import java.util.Arrays;

import javax.sound.sampled.BooleanControl;

public class IntSet {
	int[] array;
	int num;

	public void init() { 
		array = new int[4];
		num = 0;
	}
	public void add(int v) { 
		for (int i=0;i<num;i++)
		{
			if (array[i]==v){
				return;
			}
		}
		if (num < 4)
			array[num++] = v;
	}
	public boolean find(int v){
		for (int i = 0; i < num; i++) 
			if (array[i] == v) return true; 
		return false;
	}
	public int count(){
		return array.length;
	}
	public void remove(int v){
		int[] newarray = new int[4];
		int count=0;
		for (int i=0;i<num;i++)
		{
			if(array[i]==v){
				;
			}
			else{
				newarray[count++] = array[i];
			}
		}
		for (int i=0;i<num;i++)
		{
			array[i]=newarray[i];
		}
	}
	public int getIndex(int v){
		for (int i=0;i<num;i++){
			if (array[i]==v)
			{
				return i;
			}
		}
		
		return -1;
	}

}
