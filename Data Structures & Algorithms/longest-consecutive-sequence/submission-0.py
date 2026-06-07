class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        sorted_num_set = sorted(num_set)
        i = 0
        longest_seq = 1
        cur_seq = 1

        while (i + 1) < len(sorted_num_set):
            if sorted_num_set[i] == sorted_num_set[i + 1] - 1:
                cur_seq += 1
            else:
                longest_seq = max(longest_seq, cur_seq)
                cur_seq = 1
            
            i += 1
        
        return max(longest_seq, cur_seq)
        