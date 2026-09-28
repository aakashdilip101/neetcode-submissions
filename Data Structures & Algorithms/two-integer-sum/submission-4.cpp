#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];

            if (m.contains(complement)) {
                return vector<int>{m[complement], i};
            }

            m[nums[i]] = i;
        }

        return {};
    }
};
