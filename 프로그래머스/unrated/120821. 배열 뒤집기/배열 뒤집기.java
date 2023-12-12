 class Solution {
        public int[] solution(int[] num_list) {
            int[] answer = num_list;
            for (int i = 0; i < (answer.length)/2; i++) {
                int temp = answer[i];
                answer[i]=answer[(answer.length)-i-1];
                answer[(answer.length)-i-1]=temp;
            }
            return answer;
        }
    }