class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            midpoint = (l + r) // 2
            if target == nums[midpoint]:
                return midpoint
            elif target > nums[midpoint]:
                l = midpoint + 1
            else:
                r = midpoint - 1
        
        return -1
         