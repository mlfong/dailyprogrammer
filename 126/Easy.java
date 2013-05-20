import java.util.*;    
    
public class Easy {    
	public static void easy126(List<Integer> a, List<Integer> b){    
		Collections.sort(a); // O(nlogn), n=|a|    
		int bBegin = 0, aBegin = 0;    
		while(b.get(++bBegin)==0);    
		for(int j = 0; j < b.size(); j++){ // O(m) m=|b|    
			if(aBegin < a.size() && bBegin < b.size())    
				if(a.get(aBegin) < b.get(bBegin))    
					b.set(j, a.get(aBegin++));    
				else    
					b.set(j, b.get(bBegin++));    
			 else if(aBegin < a.size())    
				b.set(j, a.get(aBegin++));    
			 else    
				b.set(j, b.get(bBegin++));    
		}    
		prettyPrint(b);    
	}    
	public static void swap(List<Integer> list, int i, int j){    
		int t = list.get(i);    
		list.set(i, list.get(j));    
		list.set(j, t);    
	}    
	public static void prettyPrint(List<Integer> list){    
		for(Integer i : list)    
			System.out.print(i + " ");    
		System.out.println();    
	}    
	public static void main(String[] args){    
		List<Integer> a = new ArrayList<Integer>();    
		a.add(692);    
		a.add(1);    
		a.add(32);    
		List<Integer> b = new ArrayList<Integer>();    
		b.add(0);    
		b.add(0);    
		b.add(0);    
		b.add(14);    
		b.add(15);    
		b.add(123);    
		b.add(2431);    
		easy126(a,b);    
	}    
}