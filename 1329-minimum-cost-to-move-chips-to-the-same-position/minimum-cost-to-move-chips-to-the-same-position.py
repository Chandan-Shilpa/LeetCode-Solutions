class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        d = collections.Counter([ c % 2 for c in  position])
        return min(d[0],d[1])