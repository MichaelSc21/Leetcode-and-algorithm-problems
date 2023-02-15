class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[-1 for x in range(1,n+1)] for i in range(1, n+1)]
        print(matrix)
        
        
        r1 = 0
        r2 = n-1
        c1 = 0
        c2 = n-1 
        k = 1
        while c1 <= c2 and r1 <= r2:
            for i in range(c1, c2):
                matrix[r1][i] = k
                k += 1
            
            for i in range(r1, r2):
                matrix[i][c2] = k
                k += 1

            for i in range(c2, c1, -1):
                matrix[r2][i] = k
                k += 1

            for i in range(r2, r1, -1):
                matrix[i][c1] = k
                k += 1

        
        
        
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        if n % 2 == 1:
            matrix[r1-1][c1-1] = k

        for i in matrix:
            print(i)


solution = Solution()

solution.generateMatrix(3)
