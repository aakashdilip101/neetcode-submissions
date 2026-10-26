class Solution {
public:
    bool isPalindrome(string s) {
        size_t start = 0;
        size_t end = s.size() - 1;

        while (start < end) {
            if (!isAlphaNum(s[start])) {
                start++;
                continue;
            }

            if (!isAlphaNum(s[end])) {
                end--;
                continue;
            }

            if (tolower(s[start]) != tolower(s[end])) {
                return false;
            }

            start++;
            end--;
        }

        return true;
    }

    bool isAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
};
