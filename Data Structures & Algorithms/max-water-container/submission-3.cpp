class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int greatest = 0;

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
