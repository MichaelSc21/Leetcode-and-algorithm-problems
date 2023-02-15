class Solution:
    def applyOperations(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i] * 2
                nums[i]= 0

        return sorted(nums, key=lambda x: x==0)

solution  = Solution()
print(solution.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
        