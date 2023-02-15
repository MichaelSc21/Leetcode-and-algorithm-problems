class canConstruct():
    def recursion(self, target, wordBank):
        def recursion(target, wordBank, memo={}):
            if target in memo:
                return memo[target]
            if target == '':
                return True
            

            for word in wordBank:
                if word == target[:len(word)]:
                    memo[target] = recursion(target[len(word):], wordBank, memo)
                    if memo[target]:
                        return True

            return False
        return recursion(target, wordBank)

    def tabulation(self, target, wordBank):
        def tabulation(target, wordBank):
            table = [False for _ in range(len(target) + 1)]
            table[0] = True

            for i in range(len(table)):
                if table[i] != False:
                    for word in wordBank:
                        if i+ len(word) <= len(target):
                            if target[i:len(word)+i] == word:
                                table[i+len(word)] = True
                        #table[i + len(word)] = True

            return table[len(target)]



        return tabulation(target, wordBank)


solution = canConstruct()
print(solution.tabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(solution.tabulation('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf', ['a', 'aaa', 'aaaaaa', 'aaaaaaaa', 'abcd']))