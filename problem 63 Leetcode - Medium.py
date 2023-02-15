class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[0])-1

        mem = [[0] * len(obstacleGrid[0]) for __ in range(len(obstacleGrid))]

        if obstacleGrid[m][n] == 1:
            return 0
        def recursion(obstacleGrid, r, c):
            if r == m and c == n:
                return 1
            elif r > m or c > n or obstacleGrid[r][c]:
                return 0
            
            
            if mem[r][c]:
                return mem[r][c]
            mem[r][c] =  recursion(obstacleGrid, r+1, c) + recursion(obstacleGrid, r, c+1)
            print(mem[r][c])
            return mem[r][c]
        return recursion(obstacleGrid, 0, 0)


solution = Solution()
grid= [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]]


answer = solution.uniquePathsWithObstacles(grid)
print(answer)