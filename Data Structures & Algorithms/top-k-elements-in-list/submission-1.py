class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int);
        for num in nums:
            count[num] += 1
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        
        return output