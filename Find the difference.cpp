class Solution {
public:
    char findTheDifference(string s, string t) {
        sort(t.begin(),t.end());
        sort(s.begin(),s.end());
        int i=0;
        for( i=0;i<t.size();i++)
        {
            if(s[i]==t[i])
            continue;
            else break;
        }
           
        return t[i];
    }
};
