class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        
        int min_len = 100;
        for (int i = 0; i < size(words); i++){
            min_len = min(min_len, int(words[i].length()));
        }

        vector<string> output;
        
        int i = 0;
        while(i < words[0].length()){
            char c = words[0][i];
            bool ok = true;

            for (int j = 0; j < size(words); j++){
                if(words[j].find(c) == string::npos){
                    ok = false;
                    break;
                }
            }
            if (ok){
                string s = "";
                s += c;
                output.push_back(string(1,c));
                for (int k = 0; k < size(words); k++){
                    auto pos = words[k].find(c);
                    words[k].erase(pos,1);
                }
            }
            else{
                i++;
            }
        }
        return output;
    }
};