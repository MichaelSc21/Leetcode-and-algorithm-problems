class canSum():
    def recursion(self, target, arrayNums):
        def recursion(target, arrayNums, memo= {}):
            if target in memo:
                return memo[target]
            if target == 0:
                return True
            if target < 0:
                return False
            for i in arrayNums:
                remainder = target - i
                memo[target]=recursion(remainder, arrayNums)
                if memo[target] == True:
                    return True

            return False

        return recursion(target, arrayNums)

    def tabulation(self, target, arrayNums):
        boolList = [False for _ in range(target + 1)]
        boolList[0] = True
        #print(boolList)
        for i in range(target):
            if boolList[i] == True:
                for j in range(len(arrayNums)):
                    if i + arrayNums[j] <= target:
                        boolList[i+arrayNums[j]] = True
        


        return boolList[target]





solution = canSum()

print(solution.recursion(target = 7, arrayNums = [5, 3, 4, 7]))
print(solution.recursion(target = 364, arrayNums = [14, 7]))

print(solution.tabulation(target = 7, arrayNums = [5, 3, 4, 7]))
print(solution.tabulation(target = 300, arrayNums = [14, 7]))