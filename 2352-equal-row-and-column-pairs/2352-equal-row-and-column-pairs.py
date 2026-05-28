from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [[] for _ in range(len(grid))]
        columns = [[] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i].append(grid[i][j])
                columns[j].append(grid[i][j])
        
        counter = 0
        for k in range(len(rows)):
            for l in range(len(columns)):
                if rows[k] == columns[l]:
                    counter += 1

        return counter

