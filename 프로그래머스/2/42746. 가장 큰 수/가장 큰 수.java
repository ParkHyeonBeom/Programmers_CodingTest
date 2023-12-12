import java.util.Arrays;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] str = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new); 
        
        Arrays.sort(str, (a, b) -> (b + a).compareTo(a + b));
        
        if (str[0].equals("0")) {
            return "0";
        }
        
        for (String s : str) {
            answer += s;
        }
        return answer;
    }
}