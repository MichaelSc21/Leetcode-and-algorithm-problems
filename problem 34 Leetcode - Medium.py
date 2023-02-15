class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """



        def first(nums, target):
            first =-1
            left = 0
            right = len(nums)-1
            while left<= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    first = mid
                    right = mid-1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1

            return first  

        def last(nums, target):
            last=-1
            left = 0
            right = len(nums)-1
            while left<= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    last = mid
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1

            return last  
        return first(nums, target), last(nums, target)
solution = Solution()

nums = [5,7,7,8,8,10]
target = 8
returnval = solution.searchRange(nums, target)
print(returnval)