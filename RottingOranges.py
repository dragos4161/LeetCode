class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        fresh = set()
        rotten = collections.deque()
        step = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append([i,j,step])
        while rotten:
            i, j, step = rotten.popleft()
            for dx, dy in dirs:
                if 0 <= i+dx < row and 0 <= j +  dy < col and grid[i+dx][j+dy] == 1:
                    grid[i+dx][j+dy] = 2
                    fresh.remove((i+dx,j+dy))
                    rotten.append([i+dx,j+dy,step+1])
        return step if not fresh else -1