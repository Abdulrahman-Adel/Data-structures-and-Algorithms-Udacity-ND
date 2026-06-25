class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # the idea of that problem is that when you visit a node you're given
        # access to (x1, x2, ..) other nodes which can be possible paths for you
        # so you don't have to go one by one


        # visited = [0]

        # def traverseNode(node):
        #     for item in node:
        #         if item not in visited:
        #             visited.append(item)
        #             traverseNode(rooms[item])
            
        #     return
        
        # traverseNode(rooms[0])
        # return len(visited)==len(rooms)

        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)