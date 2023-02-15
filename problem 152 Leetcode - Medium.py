class Solution:
    def maxProduct(self, nums):
        max = - (2**31)

        prod = 1

        for i in range(len(nums)):
            prod *= nums[i]
            if max < prod:
                max = prod
            else:
                prod = 1
            if prod <= 0:
                prod = 1

        return max

solution = Solution()
#print(solution.maxProduct([2,3,-2,4]))
print(solution.maxProduct([0,2]))