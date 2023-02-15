from array import array


class LongestIncreasingSequence():
    def tabulation(self, arrayList):

        def tabulation(arrayList):

            tempArray = [1   for i in range(len(arrayList))]

            for i in range(1, len(arrayList)):
                subproblems = [tempArray[j] for j in range(i) if arrayList[j] < arrayList[i]]
                tempArray[i] = 1+ max(subproblems, default = 0)
            return max(tempArray)
        return tabulation(arrayList)

    def tabulation2(self, arrayList) -> list: # Do keep in mind the list is backwards
        def tabulation(arrayList):
            tempArray = [[i]   for i in arrayList]
            print(tempArray)
            for i in range(1, len(arrayList)):
                subproblems = [tempArray[j] for j in range(i) if arrayList[j] < arrayList[i]]
                maxVal = max(subproblems, key = lambda x: len(x), default = 'None')
                if maxVal != 'None':
                    
                    tempArray[i].extend(maxVal)
            print(tempArray)
            return max(tempArray, key= lambda x: len(x))

        return tabulation(arrayList)



solution = LongestIncreasingSequence()
print(solution.tabulation2([3, 1, 8, 2, 5]))
print(solution.tabulation2([5, 2, 8, 6, 3, 6, 9, 5]))


