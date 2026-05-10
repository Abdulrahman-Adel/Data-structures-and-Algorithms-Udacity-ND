class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        if len(flowerbed) <= 1:
            return flowerbed[0]==0
        for i in range(len(flowerbed)):
            if n ==0:
                return True
            if flowerbed[i]==1:
                continue
            if i == 0:
                if flowerbed[i + 1]==0:
                   flowerbed[i]=1
                   n -= 1
            if i == len(flowerbed)- 1:
                if flowerbed[i - 1]==0:
                   flowerbed[i]=1
                   n -= 1   
            if flowerbed[max(i-1, 0)]==0 and flowerbed[min(i+1, len(flowerbed)-1)]==0:
                flowerbed[i]=1
                n -= 1
        return n==0 