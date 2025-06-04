class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        cols = list(zip(*matrix))
        col_max = [max(c) for c in cols]
        return [[col_max[j] if val == -1 else val for j, val in enumerate(row)] for row in matrix]
