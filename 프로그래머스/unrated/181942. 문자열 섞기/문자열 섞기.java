class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        
        for(int i=0 ; i<str1.length() ; i++)
        {   
            answer = answer+str1.charAt(i);
            for(int j=0 ; j<str2.length() ; j++)
            {
                answer = answer+str2.charAt(i);
                break;
            }
        }   
        return answer;
    }
}