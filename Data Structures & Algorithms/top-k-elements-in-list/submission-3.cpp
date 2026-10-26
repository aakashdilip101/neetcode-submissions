class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }

        vector<pair<int, int>> arr;
        for (auto entry : counts) {
            pair<int, int> new_item(entry.second, entry.first);
            arr.push_back(new_item);
        }

        sort(arr.begin(), arr.end());
        vector<int> output;
        while (output.size() < k) {
            output.push_back(arr.back().second);
            arr.pop_back();
        }

        return output;
    }
};
