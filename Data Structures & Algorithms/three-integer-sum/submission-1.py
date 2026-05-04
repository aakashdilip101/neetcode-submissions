class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                target = -num
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] == target:
                    output.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                
                    while end > start and nums[end] == nums[end + 1]:
                        end -= 1
        
        return output
