class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;
        vector<int>arr;
        for(int i = 0; i < size(tokens); i++){
            if(tokens[i] == "+" || tokens[i] == "-" ||tokens[i] == "*" ||tokens[i] == "/"){
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                if (tokens[i] == "+") st.push(b+a);
                else if (tokens[i] == "-") st.push(b-a);
                else if (tokens[i] == "*") st.push(b*a);
                else if (tokens[i] == "/") st.push(b/a);
            }
            else
            st.push(std::stoi(tokens[i]));
        }
        return st.top();
    }
};