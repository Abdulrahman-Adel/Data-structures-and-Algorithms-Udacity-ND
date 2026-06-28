class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # I think we can start with initial point on the grid and we can then find
        # all adjecent nodes and see if it gets rotten or not 
        # initially maybe we should start by fining out all the positions
        # of rotten oranges

        # directions = [
        #     (1, 0),   # down
        #     (-1, 0),  # up
        #     (0, 1),   # right
        #     (0, -1)   # left
        # ]

        # rotten_oranges = []
        # fresh_oranges = []
        # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]      
        # def dfs(r, c):
        #     nonlocal rotten_oranges, fresh_oranges
        #     # boundaries
        #     if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        #         return

        #     # check if visited
        #     if visited[r][c]:
        #         return 
            
        #     # mark as visited
        #     visited[r][c] = True

        #     if grid[r][c]==2:
        #         rotten_oranges.append([r, c])
        #     elif grid[r][c]==1:
        #         fresh_oranges.append([r, c])
            
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # dfs(0, 0)

        # if not fresh_oranges:
        #     return 0
        
        # from collections import deque
        # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]    
        # def validPosition(dr, dc):
        #     if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[0]):
        #         return False
            
        #     return True if grid[dr][dc]==1 and visited[dr][dc]==False else False

        # got_rotten = []
        # def bfs(r, c):
        #     nonlocal got_rotten
        #     queue = deque()
            
        #     queue.append((r, c))
        #     visited[r][c]=True
        #     minutes = 0
        #     while queue:
        #         remove = len(queue)
        #         for item in range(remove):
        #             r, c = queue.popleft()
        #             for dr, dc in directions:
        #                 if validPosition(r+dr, c+dc):
        #                     visited[r+dr][c+dc]=True
        #                     got_rotten.append([r+dr, c+dc])
        #                     queue.append([r+dr, c+dc])
        #         if not queue:
        #             break
        #         minutes +=1
            
        #     return minutes

        # if rotten_oranges:
        #     result = bfs(rotten_oranges[0][0], rotten_oranges[0][1])
        # else:
        #     return -1
         
        # if len(got_rotten)!=len(fresh_oranges):
        #     return -1
        # return result

        # this attempt was fine but the only thing that was missing is that why don't you just start the queue of the bfs
        # with the rotten places (very simple) and you will already process all at the same time with each minute 
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        queue = deque()
        fresh = 0

        # collect initial rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while queue and fresh > 0:

            # process current minute
            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))

            minutes += 1

        return minutes if fresh == 0 else -1
        
                    

        

