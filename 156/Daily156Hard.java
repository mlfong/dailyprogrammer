import java.util.HashMap;


public class Daily156Hard
{
    
    public static void main(String[] args)
    {
        System.out.println(daily156Hard(args));
    }
    
    public static String daily156Hard(String[] flipme)
    {
        HashMap<Character, Character> flipMap = new HashMap<Character, Character>();
        String shortenedAscii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!. ";
        String flippedAscii = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄ZƖᄅƐㄣϛ9ㄥ860¿¡˙ ";
        for(int i = 0; i < shortenedAscii.length(); i++)
            flipMap.put(shortenedAscii.charAt(i), flippedAscii.charAt(i));
        StringBuilder sb = new StringBuilder();
        for(int i = flipme.length - 1; i >= 0; i--)
        {
            for(int j = flipme[i].length() - 1; j >= 0; j--)
                sb.append(flipMap.get(flipme[i].charAt(j)));
            sb.append("\n");
        }
        return sb.toString();
    }
    
}

