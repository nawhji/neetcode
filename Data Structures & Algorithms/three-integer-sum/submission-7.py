class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two sum -> find one that makes it zero

        nums.sort()
        print(nums)
        output = []

        for i in range(len(nums)):
            # find nums[j] + nums[k] that is equal to -nums[i]
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # index i would be negative,
            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    
        return output