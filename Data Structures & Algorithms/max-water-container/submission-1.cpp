class Solution {
public:
    int maxArea(vector<int>& heights) {
        size_t l = 0;
        size_t r = heights.size() - 1;
        int greatest = 0;

        while (l < r) {
            greatest = max(greatest, static_cast<int>(((r - l) * min(heights[l], heights[r]))));

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }


        }

        return greatest;
    }
};
