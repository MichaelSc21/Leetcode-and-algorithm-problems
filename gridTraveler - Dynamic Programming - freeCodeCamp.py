
class Recursion():
    def recursion(self, m, n):
        m -= 1
        n -= 1
        def gridTraveler(m, n, memo=[[0 for _ in range(n+1)] for __ in range(m+1)]):
            #print(memo)
            if 0 != memo[m][n]:
                return memo[m][n]
            if m == 0 and n ==0:
                return 1
            if m == -1 or n == -1:
                return 0
            memo[m][n] =  gridTraveler(m-1, n) + gridTraveler(m, n-1)
            return memo[m][n]
        return gridTraveler(m, n)

class Tabulation():
    def tabulation(self, m, n):
        def gridTraveler(m,n):
            table = [[0 for _ in range(n)] for __ in range(m)]
            table[0][1] = 1
            table[1][0] = 1
            for i in range(0, m):
                for j in range(0, n):
                    if j-1 >= 0: table[i][j] += table[i][j-1]
                    if i-1 >= 0 : table[i][j] += table[i-1][j]
            return table[m-1][n-1]

        return gridTraveler(m, n)
    
rec = Recursion()
print(rec.recursion(6, 5))

tab = Tabulation()
print(tab.tabulation(6, 5))
