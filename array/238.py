class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        cache_result = []
        for index, number in enumerate(nums):
            cache_result.append(pre)
            pre *= number

        pos = 1
        n = len(nums)
        for i, number in enumerate(reversed(nums)):
            original_index = n - 1 - i
            cache_result[original_index] *= pos
            pos *= nums[original_index]

        return cache_result
