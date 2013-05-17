import java.io.*;
import java.util.*;
public class Easy {
    public static void main(String[] args) throws Exception {
        // if(args==null || args.length == 0)
            // System.exit(-1);
        args = new String[10];
		args[0] = "./untitled.txt";
        BufferedReader br = new BufferedReader(new FileReader(new File(args[0])));
        String s;
        int numWords = 0, numLetters = 0, numSymbols = 0;
        HashMap<String, Integer> wordMap = new HashMap<String, Integer>();
        HashMap<Character, Integer> letterMap = new HashMap<Character, Integer>();
		HashMap<String, Integer> firstMap = new HashMap<String, Integer>();
        TreeSet<WordWrapper> mcWords = new TreeSet<WordWrapper>(Collections.reverseOrder());
        TreeSet<WordWrapper> mcLetters = new TreeSet<WordWrapper>(Collections.reverseOrder());
		TreeSet<WordWrapper> mcFirst = new TreeSet<WordWrapper>(Collections.reverseOrder());
		HashSet<Character> letters = new HashSet<Character>();
		for(char c = 'a'; c <= 'z'; c++)
			letters.add(c);
		boolean newParagraph = true;
        while(null != (s = br.readLine())) {
			if(s.length() < 1){
				newParagraph = true;
				continue;
			}
            String[] line = s.split(" ");
			if(newParagraph){
				newParagraph = false;
				String firstWord = line[0].toLowerCase();
				if(firstMap.keySet().contains(firstWord))
					firstMap.put(firstWord, firstMap.get(firstWord)+1);
				else
					firstMap.put(firstWord, 1);
				WordWrapper ww = new WordWrapper(firstMap.get(firstWord), firstWord);
				if(mcFirst.contains(ww))
					mcFirst.remove(ww);
				mcFirst.add(ww);
			}
            for(String word : line){
				if(word.length() < 1)
					continue;
				numWords++;
                word = word.toLowerCase();
                if(wordMap.keySet().contains(word))
                    wordMap.put(word, wordMap.get(word) + 1);
                else
                    wordMap.put(word, 1);
                WordWrapper ww = new WordWrapper(wordMap.get(word), word);
                if(mcWords.contains(ww))
                    mcWords.remove(ww);
                mcWords.add(ww);
                for(Character c : word.toCharArray()){
                    if(c.charValue() >= (int)'a' && c.charValue() <= (int)'z')
					{
	                    if(letterMap.keySet().contains(c))
	                        letterMap.put(c, letterMap.get(c)+1);
	                    else
	                        letterMap.put(c, 1);
	                    WordWrapper wwletter = new WordWrapper(letterMap.get(c), ""+c);
	                    if(mcLetters.contains(wwletter))
	                        mcLetters.remove(wwletter);
	                    mcLetters.add(wwletter);
						numLetters++;
						if(letters.contains(c))
							letters.remove(c);
					}

                    else if((c.charValue() < (int)'0' || c.charValue() > (int)'9') && c != ' ')
                        numSymbols++;
                    
                }
            }
        }
        System.out.println(numWords + " words");
        System.out.println(numLetters + " letters");
        System.out.println(numSymbols + " symbols");
		String[] top3Words = new String[3];
        int cc = 0;
        for(WordWrapper i : mcWords) {
			top3Words[cc++] = i.string;
			System.out.println(i);
            if(cc == 3)
				break;
        }
		String[] top3Letters = new String[3];
		cc = 0;
        for(WordWrapper i : mcLetters) {
			top3Letters[cc++] = i.string;
            if(cc == 3)
				break;
        }
		System.out.print("Top three most common words: ");
		for(String top : top3Words)
			System.out.print("\"" + top + "\" ");
		System.out.println();
		System.out.print("Top three most common letters: ");
		for(String top : top3Letters)
			System.out.print("\"" + top + "\" ");
		System.out.print("\nMost common first word(s) of a paragraph: ");
		cc = 0;
		for(WordWrapper i : mcFirst) {
			cc = i.count;
			break;
		}
		for(WordWrapper i : mcFirst) {
			if(i.count == cc)
				System.out.print("\"" + i.string + "\" ");
			else
				break;
		}
		System.out.print("\nNumber of words only used once: ");
		Iterator<WordWrapper> itr = mcWords.descendingIterator();
		while(itr.hasNext()) {
		    WordWrapper ww = itr.next();
			if(ww.count == 1)
				System.out.print("\"" + ww.string + "\" ");
		    else
				break; // we can do this b/c we're reverse iterating a max pq essentially
		}
		System.out.print("\nLetters not used in this document: ");
		for(Character c : letters) 
			System.out.print("\"" + c + "\" ");
        br.close();
    }
    
    public static void printMap(HashMap<String, Integer> hm){
        for(String s : hm.keySet()){
            System.out.println(s + ": " + hm.get(s));
        }
    }
    static class WordWrapper implements Comparable<WordWrapper>{
        public int count;
        public String string;
        public WordWrapper(int c, String s){
            this.count = c;
            this.string = s;
        }
        public String toString(){
            return this.string + " " + this.count;
        }
        public boolean equals(Object o){
            if(o instanceof WordWrapper){
                WordWrapper other = (WordWrapper)o;
                if(other==this) return true;
                return this.string.equals(other.string);
            }
            return false;
        }
		public int compareTo(WordWrapper o){
			if(this.string.compareTo(o.string) != 0) {
				return 1024*(this.count-o.count) + this.string.compareTo(o.string); // ugly hack to make frequency worth more than string
			}
			return this.string.compareTo(o.string);
		}
        public int hashCode(){
            return this.string.hashCode();
        }
    }
}


