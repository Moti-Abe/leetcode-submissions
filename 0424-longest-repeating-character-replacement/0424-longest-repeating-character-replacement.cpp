class Solution {
public:
    int characterReplacement(string s, int k) {
        map<char,int>mpp;
        int l = 0, r = 0, changes = 0;
        int maxLen = 0, maxFreq = 0, n = size(s);
        while(r < n){
            mpp[s[r]]++;
            maxFreq = max(maxFreq, mpp[s[r]]);
            while(r-l+1 - maxFreq > k){
                mpp[s[l]]--;
                if(mpp[s[l]] == 0)
                mpp.erase(s[l]);
                l++;
            }
            if(changes <= k)
            maxLen = max(maxLen, r-l+1);
            r++;
        }
        return maxLen;
    }
};