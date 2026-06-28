import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.SmallestInfiniteSet = [n for n in range(1, 1001)]
        self.seen = {}
        for n in self.SmallestInfiniteSet:
            self.seen[n]=True

    def popSmallest(self) -> int:
        element = heapq.heappop(self.SmallestInfiniteSet)
        self.seen[element]=False
        return element

    def addBack(self, num: int) -> None:
        if not self.seen.get(num):
            self.seen[num]=True
            heapq.heappush(self.SmallestInfiniteSet, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)