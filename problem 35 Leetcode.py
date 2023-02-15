class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        print(f"The last value is: {right}")
        while left<=right:
            mid = (left + right)//2
            print(f"The middle value in this search is: {mid}")
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

                

        if nums[mid] > target:
            return mid
        else:
            return mid+1


val = Solution.searchInsert([1,3,5,6], 7)
print(val)