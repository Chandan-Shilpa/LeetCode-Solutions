class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
           count = Counter(nums)
           good_pairs = 0
           for val in count.values():
             good_pairs += val * (val - 1) // 2
           return good_pairs 