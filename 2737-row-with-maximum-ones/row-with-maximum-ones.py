class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
         max_count = -1
         row_index = -1
         for i, row in enumerate(mat):
            ones = sum(row)
            if ones > max_count:
             max_count = ones
             row_index = i
         return [row_index, max_count]