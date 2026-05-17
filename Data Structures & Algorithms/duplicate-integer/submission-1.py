class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_dict = {}

        # for n in nums:
        #     if nums_dict.get(n) is None:
        #         nums_dict[n] = 1
        #     else:
        #         return True
        
        # return False

        if len(set(nums)) == len(nums):
            return False
        else:
            return True