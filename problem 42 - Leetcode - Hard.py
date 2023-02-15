class Solution:
    def trap(self, height) -> int:
        l ,r= 0, len(height)-1
        maxLeft= height[l]
        maxRight = height[r]
        res = 0

        while l<r:
            if maxLeft < maxRight:
                l+=1
                maxLeft= max(height[l], maxLeft)
                res += maxLeft - height[l]

            else:
                r-=1
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]

        return res

    def trap2(self, height):

        tallest = height[0]
        tallest_index = 0
        running_area = 0
        area = 0
        for i in range(1, len(height)):
            if height[i] >=  tallest:
                tallest = height[i]
                tallest_index= i
                area += running_area
                running_area = 0 
            else:
                running_area += tallest - height[i]

        tallest = height[-1]
        running_area = 0
        for j in range(len(height)-2, tallest_index-1, -1):
            if height[j] >= tallest:
                tallest = height[j]
                area += running_area
                running_area = 0
            else:
                running_area += tallest - height[j]
        return area
        
solution = Solution() 
#print(solution.trap2([0,1,0,2,1,0,1,3,2,1,2,1])) # returns 6
#print(solution.trap([4,2,0,3,2,5])) # returns 9
print(solution.trap([2,0,2]))