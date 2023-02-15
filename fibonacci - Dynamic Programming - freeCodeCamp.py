class Recursion():
    def recursion(self, n):
        def fib(n, memo={}):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n

            memo[n] =  fib(n-2) + fib(n-1)
            return memo[n]
        
        return(fib(n))

class Tabulation():
    def tabulation(self, n):
        def fib(n):
            tabList = []
            for i in range(n+1):
                if i <= 1:
                    tabList.append(i)
                else:
                    tabList.append(tabList[i-1] + tabList[i-2] )
            return(tabList[n])
        return fib(n)


rec = Recursion()
print(rec.recursion(6))

tab = Tabulation()
print(tab.tabulation(6))