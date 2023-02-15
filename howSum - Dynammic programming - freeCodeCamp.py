class howSum():
    def recursion(self, target, nums):
        
        def recursion( target, nums, memo={}):
            if target in memo: 
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None

            for i in nums:
                remainder = target - i
                memo[target] = recursion(remainder, nums)
                if memo[target] != None:
                    memo[target].append(i)
                    
                    return memo[target]
            return None
        return recursion(target, nums)





    def tabulation(self, target, nums):
        def tabulation(target, nums):
            table = [None for _ in range(target+1)]
            table[0] = []

            for i in range(len(table)):
                if table[i] != None:
                    for j in range(len(nums)):
                        if i+nums[j] <= target:
                            if type(table[i+nums[j]]) == type([]):
                            
                                table[i+nums[j]].append(nums[j])
                            else:
                                table[i+nums[j]] = [nums[j]]
                    if table[target] != None:
                        return table[target]
            return table[target]
        return tabulation(target, nums)






solution = howSum()
print(solution.recursion(target = 7, nums= [5, 3, 4, 7]))
print(solution.recursion(target = 300, nums= [14, 7]))
print(solution.tabulation(target=  7, nums = [5, 3, 4, 7]))