class Solution {
    public int solution(int a, int b) {
        
        String x = String.valueOf(a);
        String y = String.valueOf(b);
        String w = x+y;
        String z = y+x;    
        
        return Math.max(Integer.valueOf(w) , Integer.valueOf(z));
    }
}