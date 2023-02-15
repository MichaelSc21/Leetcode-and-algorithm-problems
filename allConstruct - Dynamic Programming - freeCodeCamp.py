class allConstruct():
    def recursion(self,target, wordBank) -> int:
        
        def recursion(target, wordBank, memo={}):
            if target in memo:
                return memo[target]
            if target=='':
                return [[]]
            rList = []
            count = 0
            for word in wordBank:
                if target[:len(word)] == word:  
                    currList = dfs(target[len(word):], wordBank, memo)
                    #print(f"Recursive call number: {count}")
                    #targetList = map(lambda List: List.insert(0, word), currList)
                    #currList.insert(0, word)
                    for i in currList:
                        i.insert(0, word)
                    #print(currList)
                    rList.extend(currList)
                    #print(f"rList is: {rList}")
                count += 1
            #rList.append(targetList)
            #rList.extend(currList)
            #print(f"rList outside the loop is: {rList}")
            memo[target] = rList
            return rList

        print(f"rList is: {recursion(target, wordBank)}")

    def tabulation(self, target, wordBank):
        def tabulation(target, wordBank):
            table = [[] for _ in range(len(target) + 1)]
            table[0] = [[]]

            for i in range(len(table)):

                    for word in wordBank:
                        if i + len(word) <= len(target):
                            if target[i:len(word)+i] == word:
                                for elem in table[i]:
                                    tempList = [*elem, word]
                                    table[i+len(word)]  += [tempList]
                        #table[i + len(word)] = True

            return table[len(target)]

        return tabulation(target, wordBank)
        
        


solution = allConstruct()
print(solution.tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(solution.tabulation('aaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aaaa', 'aaaaaa', 'aa']))