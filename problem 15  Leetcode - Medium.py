class Solution():
    def threeSum(self,  nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue


            l, r  = i+1, len(nums)-1
            while l<r:
                target = nums[i] + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1 
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-2, -2, 0, 0, 1, 1, 2, 2]))
    print(solution.threeSum([-1,0,1,2,-1,-4]))