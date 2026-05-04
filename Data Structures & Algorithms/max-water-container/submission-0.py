class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        greatest = -1

        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            if area > greatest:
                greatest = area

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        

        return greatest