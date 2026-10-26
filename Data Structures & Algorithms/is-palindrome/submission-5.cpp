class Solution {
public:
    bool isPalindrome(string s) {
        size_t start = 0;
        size_t end = s.size() - 1;

        while (start < end) {
            while (start < end && !isAlphaNum(s[start])) {
                start++;
            }

            while (end > start && !isAlphaNum(s[end])) {
                end--;
            }

            if (tolower(s[start]) != tolower(s[end])) {
                return false;
            }

            start++;
            if (end == 0) {
                break;
            }
            end--;
        }

        return true;
    }

    bool isAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
};
