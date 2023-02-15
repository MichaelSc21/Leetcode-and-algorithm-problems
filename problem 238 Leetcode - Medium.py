class Solution:
    def productExceptSelf(self, nums):
        list1 = [1]

        for i in range(0, len(nums)-1):
            temp = nums[i]*list1[-1] 
            list1.append(temp)

        list2 = [1 for _ in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            list2[j] = nums[j+1] * list2[j+1]
            #list2.append(temp)
        list3 = []
        for k in range(len(nums)):
            list3.append(list1[k] * list2[k])
        return list3

    def productExceptSelf2(self, nums):
        retList = [1]
        prefix = 1
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                count += 1
            prefix *= nums[i]
            retList.append(prefix)
        prod = 1
        if count > 1:
            return [0 for _ in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            prod *= nums[j+1]
            retList[j] *= prod

        return retList

solution = Solution()
print(solution.productExceptSelf2([1,2,3,4]))