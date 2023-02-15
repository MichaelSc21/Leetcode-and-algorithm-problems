from itertools import count


class countConstruct():
    def recursion(self, target, wordBank):
        def recursion(target, wordBank):
            if target == '':
                return 1
            count = 0
            for word in wordBank:
                if word == target[:len(word)]:
                    res = recursion(target[len(word):], wordBank)
                    #if type(res) == type(int): 
                    count += res
                    
            return count
        return recursion(target, wordBank)

    def tabulation(self, target, wordBank):
        def tabulation(target, wordBank):
            table = [0 for _ in range(len(target) + 1)]
            table[0] = 1

            for i in range(len(table)):
                if table[i] != 0:
                    for word in wordBank:
                        if i+ len(word) <= len(target):
                            if target[i:len(word)+i] == word:
                                table[i+len(word)] += table[i]
                        #table[i + len(word)] = True

            return table[len(target)]


        return(tabulation(target, wordBank))


solution = countConstruct()
print(solution.tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))