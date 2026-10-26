class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hm;

        for (const auto& str : strs) {
            vector<int> counts(26, 0);

            for (char c : str) {
                counts[c - 'a']++;
            }

            string key;
            key.append(to_string(counts[0]));
            for (size_t i = 0; i < 26; ++i) {
                key.append(',' + to_string(counts[i]));
            }

            hm[key].push_back(str);
        }

        vector<vector<string>> output;
        for (const auto& entry : hm) {
            output.push_back(entry.second);
        }

        return output;
    }
};
