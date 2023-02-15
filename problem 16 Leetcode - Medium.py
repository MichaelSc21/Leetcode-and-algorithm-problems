class Solution():
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        closest_diff = 2**31
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < target:
                    l+= 1
                    diff = target -sum
                elif sum > target:
                    r -= 1
                    diff = sum - target
                else:
                    return sum 
                if diff < closest_diff:
                    closest_diff = diff
                    closest_sum = sum
        return closest_sum



solution = Solution()
#print(solution.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(solution.threeSumClosest(nums = [0,0,0], target = 1))
print(solution.threeSumClosest([1,1,1,0], target = -100))