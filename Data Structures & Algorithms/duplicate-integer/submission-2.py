class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_dict = {}

        # for n in nums:
        #     if nums_dict.get(n) is None:
        #         nums_dict[n] = 1
        #     else:
        #         return True
        
        # return False

        nums_set = set()

        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        return False