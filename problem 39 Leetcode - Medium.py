class Solution():
    def combinationSum(self, target, candidates):


        def recursion(target, candidates, memo= {}):
            if target in memo:
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None
            rList = []
            for i in candidates:
                memo[target] = recursion(target - i, candidates, memo)
                if memo[target] != None:
                    memo[target].append(i)
                    print(memo)
                    #return memo[target]
            return memo[target]
        return recursion(target, candidates)


    def combinationSum(self, target, candidates):
        def tabulation(target, candidates):

            table = [[] for _ in range(target+1)]
            table[0]= [[]]

            for i in range(len(table)):
                if table[i] != []:
                    for nums in candidates:
                        if i+nums <= target:
                            for elems in table[i]:
                                if [*elems, nums] not in table[i+nums]:
                                    table[i+nums].append([*elems, nums])
            return table[target]
        

        def method2(candidates, target,idx=0, path=[]):
            idx = 0
            res=[]
            if target < 0:
                return 
            if target == 0:
                res.append(path)
                return 
                
            for i in range(idx, len(candidates)):
                method2(candidates[i:], target-candidates[i],i, path.extend(candidates[i]))


        return method2(candidates, target)

            



solution = Solution()

#solution.combinationSum(target = 300, candidates = [7, 14])
print(solution.combinationSum(target = 7, candidates = [2,3,6, 7]))
print(solution.combinationSum(target = 8, candidates = [2,3,5]))