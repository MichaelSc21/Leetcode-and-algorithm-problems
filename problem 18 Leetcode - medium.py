class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        k = len(nums)
        if not nums:
            return res
        avg = target/4
        if nums[0] > avg or nums[-1] < avg:
            return res
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, len(nums)):
                if j<len(nums)-1 and j>i+1 and nums[j] == nums[j-1]:
                    continue
                l, r  = j+1, len(nums)-1
                while l<r:
                    foursum = nums[j] + nums[l] + nums[r] + nums[i]
                    if foursum > target:
                        r -= 1
                    elif foursum  < target:
                        l += 1
                    else:
                        res.append([nums[i],nums[j],  nums[l], nums[r]])
                        l+=1 
                        while l<r and nums[l] == nums[l-1]:
                            l +=1


        return res
solution = Solution()
print(solution.fourSum(nums = [2,2,2,2,2], target = 8))
#print(solution.fourSum([1,0,-1,0,-2,2], target=0))
print(solution.fourSum([-2,-1,-1,1,1,2,2], target=  0))
        