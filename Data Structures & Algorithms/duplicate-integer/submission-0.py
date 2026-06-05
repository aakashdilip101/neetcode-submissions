class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        set_size = 0

        for num in nums:
            set_size = len(num_set)
            num_set.add(num)
            if len(num_set) == set_size:
                return True
        
        return False