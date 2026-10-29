class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix_product = [0]*len(nums)
        suffix_product = [0]*len(nums)

        prefix_product[0] = suffix_product[len(nums)-1] = 1
        
        for i in range(1,len(nums)):
            prefix_product[i] = nums[i-1]*prefix_product[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix_product[i] = nums[i+1]*suffix_product[i+1]

        for i in range(len(nums)):
            res[i] = prefix_product[i]*suffix_product[i]

        return res