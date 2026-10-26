class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mapping = {
            {'}', '{'},
            {')', '('},
            {']', '['}
        };

        for (char c : s) {
            if (c == '}' || c == ')' || c == ']') {
                if (st.empty() || st.top() != mapping[c]) {
                    return false;
                }

                st.pop();
            } else {
                st.push(c);
            }
        }

        if (!st.empty()) {
            return false;
        }

        return true;
    }
};
