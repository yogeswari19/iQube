class Solution {
    public int firstUniqChar(String s) {
        char[] ch = s.toCharArray();
        int ind=0;
        for(int i=0;i<ch.length;i++){
            if(ch[i]!=ch[i+1])
                 ind=i;
            break;
        }
        return ind;
    }
}
