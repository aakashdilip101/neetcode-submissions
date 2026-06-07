from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        output = []
        
        for item, _ in num_count.most_common(k):
            output.append(item)
        
        return output
        