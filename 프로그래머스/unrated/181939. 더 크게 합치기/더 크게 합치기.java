class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String x = Integer.toString(a) + Integer.toString(b);
        String y = Integer.toString(b) + Integer.toString(a);
        int w = Integer.parseInt(x);
        int z = Integer.parseInt(y);
        
        if(w>z)
            answer = answer + w;
        else if (w==z)
             answer = answer + w;
        else   
             answer = answer + z;
            
        return answer;
    }
}