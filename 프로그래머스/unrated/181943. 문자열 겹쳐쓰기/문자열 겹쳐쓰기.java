class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String part1 = my_string.substring(0, s);
        String part2 = my_string.substring(s + overwrite_string.length());
        
        answer = part1 + overwrite_string + part2;
        
        return answer;
    }
}