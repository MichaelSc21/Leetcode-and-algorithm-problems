class Solution:
    def maxArea(self, height) -> int:
        res, l , r ,width= 0, 0, len(height)-1, len(height)-1
        for w in range(width, 0, -1):
            if height[l] < height[r]:
                res, l= max(res, height[l] * w), l+1

            else:
                res, r = max(res, height[r] * w), r-1

        return res
solution = Solution()
print(solution.maxArea([1,1]))
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) # returns 49