class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = 0

        while l <= r:
            mid = (l + r) // 2

            if l == r:
                pivot = mid
                break
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        if nums[pivot] == target:
            return pivot

        l = 0
        r = pivot - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l = pivot + 1
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        

        return -1
            
        