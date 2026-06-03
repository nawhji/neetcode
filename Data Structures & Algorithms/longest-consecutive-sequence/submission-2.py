class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        nums_cnt = {}
        for n in nums_set:
            nums_cnt[n] = 1

        longest = 0

        for n in nums_set:
            if nums_cnt.get(n-1) is None:
                i = n
                cur_len = 1
                while nums_cnt.get(i+1) != None:
                    i += 1
                    cur_len += 1
                longest = max(longest, cur_len)
                
        return longest