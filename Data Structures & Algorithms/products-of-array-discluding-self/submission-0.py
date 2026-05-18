class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_idx = -1
        prod = 1
        prod_temp = 1

        for i in range(len(nums)):
            if zero_count == 0:
                prod_temp = prod
                # print(prod_temp, i, nums[i])
            else:
                prod_temp *= nums[i]
            prod *= nums[i]

            if nums[i] == 0:
                zero_count += 1
                zero_idx = i
        
        output = [0] * len(nums)
        if zero_count == 0:
            for i in range(len(nums)):
                # if zero_idx == i:
                #     output[i] = prod_temp
                # else:
                output[i] = prod // nums[i]
        elif zero_count == 1:
            output[zero_idx] = prod_temp
        
        return output
