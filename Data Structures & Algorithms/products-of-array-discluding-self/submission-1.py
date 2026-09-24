class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # 1. Store the product of everything to the LEFT of i
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        # 2. Multiply by the product of everything to the RIGHT of i
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output