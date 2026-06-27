from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # neighbours = defaultdict(list)
        # visited = set()
        # changes = 0
        # for a, b in connections:
        #     neighbours[a].append(b)
        #     neighbours[b].append(a)
        
        # def dfs(city):
        #     nonlocal visited, changes, neighbours, connections
        #     for neighbour in neighbours[city]:
        #         if neighbour in visited:
        #             continue
        #         if [neighbour, city] not in connections:
        #             changes += 1
        #         visited.add(neighbour)
        #         dfs(neighbour) 
        # visited.add(0)
        # dfs(0)
        # return changes


        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], -1))
        visited = [False] * n
        minChange = [0]
        def dfs(adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int):
            visited[currCity] = True
            for neighbourCity in adj[currCity]:
                if not visited[neighbourCity[0]]:
                    if neighbourCity[1] == 1:
                        minChange[0] += 1
                    dfs(adj, visited, minChange, neighbourCity[0])
        dfs(adj, visited, minChange, 0)
        return minChange[0]

        

        