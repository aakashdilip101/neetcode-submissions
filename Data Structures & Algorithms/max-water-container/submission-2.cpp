class Solution {
public:
    int maxArea(vector<int>& heights) {
        size_t l = 0;
        size_t r = heights.size() - 1;
        size_t greatest = 0;

        while (l < r) {
            greatest = max(greatest, ((r - l) * min(heights[l], heights[r])));

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }


        }

        return greatest;
    }
};
