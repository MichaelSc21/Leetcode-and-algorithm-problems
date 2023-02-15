

class bestSum():
    def bestSum(self, target, nums):

        
        def dfs(target, nums, memo={}):
            if target in memo:
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None
            shortestList = None
            for i in nums:
                remainder = target - i
                res = dfs(remainder, nums, memo)
                if res != None:
                    res.append(i)
                    currList = res
                    if shortestList == None or len(shortestList) > len(currList) :
                        shortestList = currList
            memo[target] = shortestList
            return shortestList

        print(dfs(target, nums))


    def recursion(self, target, nums):
        def recursion(target, nums, memo = {}):
            if target in memo:
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None
            
            shortestList = None
            for i in nums:
                remainder = target - i
                res= recursion(remainder, nums,memo)
                if res != None:
                    res += [i]
                    print(f"current res is: {res}")
                    if shortestList == None or len(shortestList) > len(res):
                        shortestList =res
                    
            memo[target] = shortestList
            
            print(f"the shrotes list is : {shortestList}")
            return  shortestList
        return recursion(target, nums)

    def tabulation(self, target, nums):
        def tabulation(target, nums):
            table = [None for _ in range(target+1)]
            table[0] = []
            combo = None
            for i in range(len(table)):
                if table[i] != None:
                    for num in nums:
                        if num + i <= target:

                            combo = table[i] + [num]
                            if table[i+num] == None or len(combo) < len(table[i+num]):
                                table[i+num] = combo
                       

            return table[target]
        return tabulation(target, nums)
        


solution = bestSum()
print(solution.recursion(target = 8, nums = [5, 4, 1]))
#solution.bestSum(target = 300, nums = [7, 14])
#print(solution.recursion(target = 7, nums = [2,3,6]))
#solution.bestSum(target = 8, nums = [2,3,5])
print(solution.recursion(target = 50, nums = [25, 5]))