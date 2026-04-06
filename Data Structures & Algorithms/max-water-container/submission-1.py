class Solution:
    def maxArea(self, heights: List[int]) -> int:
        dist = len(heights)-1
        max_water = 0
        l , r = 0, len(heights)-1
        while l < r:
            water = min(heights[l], heights[r]) * dist
            max_water = max(water, max_water)
            
            if heights[l] > heights[r]:
                r-=1
                dist -= 1
            elif heights[l] < heights[r]:
                l+=1
                dist -= 1
            else:
                l+=1
                r-=1
                dist -= 2

        return max_water