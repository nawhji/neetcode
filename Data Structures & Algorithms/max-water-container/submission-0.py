class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # amount of water when i, j th bars was chosen
        # (j-i) * min(heights[i], heights[j])

        l = 0
        r = len(heights)-1

        amount = 0

        while l < r:
            amount = max(amount, (r-l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]: # we dont have to move the right ptr, cur amount is the max one with this left ptr
                l += 1
            else:
                r -= 1
        
        return amount