class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>=2:
            stones.sort()
            difference=stones.pop()-stones.pop()
            if difference!=0:
                stones.append(difference)
        if len(stones)==0:
            return 0
        for i in stones:
            return i
        
            

        
        