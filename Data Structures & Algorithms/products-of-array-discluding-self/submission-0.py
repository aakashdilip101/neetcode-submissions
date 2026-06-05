class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1]
        postfix = [1]

        prev_product = 1
        i = 1

        nums_len = len(nums)

        while i < nums_len:
            prev_product *= nums[i - 1]
            prefix.append(prev_product)
            i += 1
        
        prev_product = 1
        i = nums_len - 2

        while i >= 0:
            prev_product *= nums[i + 1]
            postfix.append(prev_product)
            i -= 1
        
        for i in range(nums_len):
            output.append(prefix[i] * postfix[nums_len - 1 - i])

        return output